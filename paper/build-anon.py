#!/usr/bin/env python
"""Build the double-anonymous review copy that Synthese requires.

Synthese reviews double-anonymous and puts the burden on the author: names,
affiliations, and any other identifying information must be out of the
manuscript and out of every accompanying file, and self-citations must not be
phrased so as to reveal the author.

Third-person self-citation is permitted and is what this paper does. What is
NOT permitted, and what a plain \anontrue build still leaks, lives in the
bibliography: the repository URLs carry the author's account name, and the
foundation document carries the author's institution. This script rewrites
those five entries for the review copy.

    python build-anon.py        writes dpe-anon.tex and refs-anon.bib
    then: pdflatex dpe-anon && bibtex dpe-anon && pdflatex dpe-anon x2

Run check-anon.py afterwards. It greps the built PDF for the leak patterns and
is the thing to trust, not this script.
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# The self-cited entries. Each is the author's own artifact, so each is
# rewritten to an anonymous form that still identifies WHICH artifact is meant,
# because the argument depends on the reader being able to tell the five apart.
SELF_KEYS = {
    "bond2026pe": "Philosophy Engineering foundation document",
    "bond2026get": "Geometric Evaluation Theory research repository",
    "bond2026radar": "symbolic structure search research repository",
    "bond2026tcss": "geometric prediction of economic behaviour",
    "bond2026odline": "observational discovery campaign record",
}

WITHHELD = "Details withheld for double-anonymous review"


def anonymize_bib(src: str) -> str:
    """Rewrite the self-cited entries. Every other entry passes through."""
    out, n = [], 0
    for block in re.split(r"(?m)^(?=@)", src):
        m = re.match(r"@\w+\{([^,]+),", block)
        if not m or m.group(1).strip() not in SELF_KEYS:
            out.append(block)
            continue
        n += 1
        key = m.group(1).strip()
        year = re.search(r"year\s*=\s*\{(\d{4})\}", block)
        title = re.search(r"title\s*=\s*\{(.+?)\}\s*,?\s*\n", block, re.S)
        # Keep the title, since the five artifacts must stay distinguishable,
        # but drop author, institution, journal and every URL.
        t = " ".join(title.group(1).split()) if title else SELF_KEYS[key]
        out.append(
            "@misc{%s,\n"
            "  author       = {{Anonymous}},\n"
            "  title        = {%s},\n"
            "  howpublished = {%s},\n"
            "  year         = {%s}\n"
            "}\n\n" % (key, t, WITHHELD, year.group(1) if year else "2026")
        )
    if n != len(SELF_KEYS):
        sys.exit("expected %d self-cited entries, rewrote %d"
                 % (len(SELF_KEYS), n))
    return "".join(out)


def main() -> int:
    bib = io.open(os.path.join(HERE, "refs.bib"), encoding="utf-8").read()
    anon_bib = anonymize_bib(bib)
    leaks = re.findall(r"ahb-sjsu|San Jos|andrew\.bond|Bond", anon_bib)
    # Only non-self entries may still say Bond, and none do; assert it.
    if leaks:
        sys.exit("refs-anon.bib still contains: %s" % sorted(set(leaks)))
    io.open(os.path.join(HERE, "refs-anon.bib"), "w",
            encoding="utf-8", newline="\n").write(anon_bib)

    tex = io.open(os.path.join(HERE, "dpe.tex"), encoding="utf-8").read()
    if "\n\\anonfalse\n" not in tex:
        sys.exit("dpe.tex does not carry the \\anonfalse switch")
    tex = tex.replace("\n\\anonfalse\n", "\n\\anontrue\n", 1)
    tex = tex.replace("\\bibliography{refs}", "\\bibliography{refs-anon}", 1)
    io.open(os.path.join(HERE, "dpe-anon.tex"), "w",
            encoding="utf-8", newline="\n").write(tex)

    print("wrote dpe-anon.tex and refs-anon.bib")
    print("now: pdflatex dpe-anon && bibtex dpe-anon && pdflatex dpe-anon x2")
    print("then: python check-anon.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
