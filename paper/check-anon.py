#!/usr/bin/env python
"""Check the built review copy for identifying information.

This is the thing to trust before submitting, because it reads the PDF that
would actually be uploaded rather than the source that was meant to produce it.
A build that skipped a step, or a stale .bbl left over from the named build,
shows up here and nowhere else.

    python check-anon.py [dpe-anon.pdf]

Exit 0 when clean, 1 when a pattern is found. Needs pdftotext on PATH.
"""
import os
import re
import subprocess
import sys
import tempfile

# Each pattern is something that appears in the named build and must not appear
# in the review copy. Third-person citation of the author's prior work is
# permitted by the policy, so a bare surname in a reference list is not on this
# list; the account name, the institution, and the address are.
PATTERNS = [
    (r"ahb-sjsu", "repository account name"),
    (r"github\.com", "repository URL"),
    (r"San Jos", "author institution"),
    (r"andrew\.bond|@sjsu\.edu", "author address"),
    (r"Andrew H\. Bond", "author name"),
    (r"\bthe author\b", "first-person-adjacent self reference"),
    (r"orcid", "author identifier"),
]


def main() -> int:
    pdf = sys.argv[1] if len(sys.argv) > 1 else "dpe-anon.pdf"
    if not os.path.isfile(pdf):
        print("not found: %s (run build-anon.py and pdflatex first)" % pdf)
        return 1
    with tempfile.TemporaryDirectory() as d:
        txt = os.path.join(d, "out.txt")
        r = subprocess.run(["pdftotext", pdf, txt], capture_output=True)
        if r.returncode != 0:
            print("pdftotext failed: %s" % r.stderr.decode("utf-8", "replace"))
            return 1
        body = open(txt, encoding="utf-8", errors="replace").read()

    findings = []
    for pat, why in PATTERNS:
        hits = re.findall(pat, body, re.I)
        if hits:
            findings.append((pat, why, len(hits)))

    print("=" * 62)
    print("anonymity check: %s" % pdf)
    print("=" * 62)
    if not findings:
        print("  clean, %d patterns checked" % len(PATTERNS))
        print("=" * 62)
        return 0
    for pat, why, n in findings:
        print("  [LEAK ] %-28s %s (%d)" % (pat, why, n))
    print("=" * 62)
    print("NOT SUBMITTABLE: %d pattern(s) found" % len(findings))
    return 1


if __name__ == "__main__":
    sys.exit(main())
