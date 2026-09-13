# Submitting to *Synthese*

Two files go up. Synthese reviews double-anonymous and asks the author to
anonymize the manuscript and every accompanying file, with the identity carried
on a separate title page.

| Upload | Built from | Carries the identity |
|---|---|---|
| `paper/dpe-anon.pdf` — the manuscript | `dpe.tex` with `\anontrue`, via `build-anon.py` | no |
| `paper/title-page.pdf` — the title page | `title-page.tex` | yes |

`submission/` holds a copy of both under upload-friendly names. It is not
tracked, being byte-identical to the two files above.

## Build it

```
cd paper
rm -f *.aux *.bbl *.blg *.log *.out dpe-anon.tex dpe-anon.pdf refs-anon.bib
python build-anon.py
pdflatex dpe-anon && bibtex dpe-anon && pdflatex dpe-anon && pdflatex dpe-anon
pdflatex title-page
python check-anon.py
```

Delete the intermediates first. The failure this guards against is a `.bbl` left
over from the named build, which produces a manuscript that looks anonymous in
the source and names the author in the reference list.

## What the check covers, and what it does not

`check-anon.py` reads the built PDF rather than the source, across three layers.

- **text**, what `pdftotext` extracts, which is what a reader sees.
- **raw**, the file's bytes, which can carry an absolute source path naming the
  machine's user account.
- **metadata**, the document info dictionary, which `hyperref` fills from
  `\author` and which no text-layer check would ever look at.

It does not and cannot check whether a description in the body identifies the
author to someone who knows the field. Two judgments of that kind were made by
hand and are recorded here so they are not undone by accident.

- Third-person citation of the author's own prior work is permitted by the
  policy and the paper relies on it heavily, since its evidence is the author's
  own programme. The five self-citations appear as `Anonymous 2026a` to `2026e`,
  with titles kept so a reader can still tell the five artifacts apart, which the
  argument of Section 7 needs.
- Section 7.3 says "accepted by a systems journal" rather than naming the venue,
  and the anonymized bibliography entry drops the journal. The named build says
  both.

## Before submitting

1. Fill the volume, issue, and pages of the systems-journal reference in
   `refs.bib` if they have been assigned. The entry carries a live
   `% verify vol/issue/pages on final` mark, which is the only one left and must
   not be removed until the numbers are real.
2. Run `check-anon.py` on the file you are actually uploading, not on the one in
   `paper/`. It takes a path argument for exactly this reason.
3. Confirm the title page still carries the author, affiliation, ORCID,
   declarations, and the statement on the use of generative artificial
   intelligence. The anonymity check verifies the manuscript is clean and says
   nothing about whether the title page is complete.

## State

21 pages named, 20 anonymized, about 10,000 words, inside the 15 to 30 printed
pages Synthese expects. Both builds compile with no undefined references or
citations and no BibTeX errors or warnings. Nothing has been submitted.
