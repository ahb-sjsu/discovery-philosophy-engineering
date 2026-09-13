#!/usr/bin/env python
"""Check the built review copy for identifying information.

This is the thing to trust before submitting, because it reads the PDF that
would actually be uploaded rather than the source that was meant to produce it.
A build that skipped a step, or a stale .bbl left over from the named build,
shows up here and nowhere else.

Three layers are checked, because a clean text layer is not a clean PDF:

    text      what pdftotext extracts, which is what a reader sees
    metadata  /Author, /Title, /Creator and the rest of the document info
    raw       the file's bytes, which can carry source paths and font names

    python check-anon.py [dpe-anon.pdf]

Exit 0 when clean, 1 when a pattern is found. Needs pdftotext on PATH.
"""
import os
import re
import subprocess
import sys
import tempfile

# Each pattern appears in the named build and must not appear in the review
# copy. Third-person citation of the author's prior work is permitted by the
# policy, so a bare surname in a reference list is not here; the account name,
# the institution and the address are.
TEXT_PATTERNS = [
    (r"ahb-sjsu", "repository account name"),
    (r"github\.com", "repository URL"),
    (r"San Jos", "author institution"),
    (r"andrew\.bond|@sjsu\.edu", "author address"),
    (r"Andrew H\. Bond", "author name"),
    (r"\bthe author\b", "first-person-adjacent self reference"),
    (r"orcid", "author identifier"),
]

# The same identities, plus the things only bytes carry. A source path names
# the machine's user account and often the project directory.
RAW_PATTERNS = TEXT_PATTERNS + [
    (r"[A-Za-z]:\\\\|/Users/|/home/", "absolute source path"),
    (r"discovery-philosophy-engineering", "project directory name"),
]

INFO_KEYS = (b"Author", b"Title", b"Subject", b"Keywords")


def scan(body, patterns, label, findings):
    for pat, why in patterns:
        hits = re.findall(pat, body, re.I)
        if hits:
            findings.append((label, pat, why, len(hits)))


def main() -> int:
    pdf = sys.argv[1] if len(sys.argv) > 1 else "dpe-anon.pdf"
    if not os.path.isfile(pdf):
        print("not found: %s (run build-anon.py and pdflatex first)" % pdf)
        return 1

    findings = []

    with tempfile.TemporaryDirectory() as d:
        txt = os.path.join(d, "out.txt")
        r = subprocess.run(["pdftotext", pdf, txt], capture_output=True)
        if r.returncode != 0:
            print("pdftotext failed: %s" % r.stderr.decode("utf-8", "replace"))
            return 1
        scan(open(txt, encoding="utf-8", errors="replace").read(),
             TEXT_PATTERNS, "text", findings)

    raw = open(pdf, "rb").read()
    scan(raw.decode("latin-1"), RAW_PATTERNS, "raw", findings)

    # Document info dictionary. Empty is what the anonymous build should give,
    # since \author is empty and hyperref has nothing to embed.
    for key in INFO_KEYS:
        for m in re.finditer(rb"/" + key + rb"\s*\(([^)]{0,200})\)", raw):
            val = m.group(1).decode("latin-1").strip()
            if val:
                findings.append(("meta", key.decode(),
                                 "non-empty /%s: %r" % (key.decode(), val), 1))

    print("=" * 66)
    print("anonymity check: %s" % pdf)
    print("=" * 66)
    if not findings:
        print("  clean")
        print("  text     %d patterns" % len(TEXT_PATTERNS))
        print("  raw      %d patterns" % len(RAW_PATTERNS))
        print("  metadata %d info keys, all empty" % len(INFO_KEYS))
        print("=" * 66)
        return 0
    for layer, pat, why, n in findings:
        print("  [LEAK ] %-8s %-32s %s (%d)" % (layer, pat, why, n))
    print("=" * 66)
    print("NOT SUBMITTABLE: %d finding(s)" % len(findings))
    return 1


if __name__ == "__main__":
    sys.exit(main())
