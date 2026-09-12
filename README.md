# Discovery Philosophy Engineering

Source repository for the paper *Discovery Philosophy Engineering: Making Philosophical
Claims Experimentally Interrogable* (A. H. Bond, draft September 2026).

DPE is the discovery arm of Philosophy Engineering. Philosophy Engineering translates a
philosophical commitment into a constraint a machine can enforce. DPE runs that translation
in reverse, using the implementation as an instrument to put empirical pressure back on the
commitment. The loop is six verbs. Formalize, derive, search, probe, witness, revise.

## Layout

```
paper/dpe.tex         the manuscript
paper/refs.bib        24 references
paper/title-page.tex  the separate title page Synthese requires
paper/build-anon.py   generates the double-anonymous review copy
paper/check-anon.py   greps the built review PDF for identifying information
PROVENANCE.md         what is the author's original text, what was restored, what is new
```

## Target venue

*Synthese*. It publishes long methodological work, tolerates formalism, and the
paper argues inside its literature. Review is double-anonymous, papers run 15 to
30 printed pages, and a separate title page carries the author information.

Build the review copy and check it before submitting. `check-anon.py` reads the
PDF that would actually be uploaded rather than the source meant to produce it,
which is what catches a stale `.bbl` left over from the named build.

```
python build-anon.py
pdflatex dpe-anon && bibtex dpe-anon && pdflatex dpe-anon && pdflatex dpe-anon
python check-anon.py
```

Third-person citation of the author's prior work is permitted under the policy
and the paper relies on it. What is not permitted, and what a naive anonymous
build still leaks, is in the bibliography, where the repository URLs carry the
author's account name and the foundation document carries the institution.
`build-anon.py` rewrites those five entries. The check found the leak, and then
found a second one in the phrase "the author's hands", which was generic but
readable as self-reference and is now "the claimant's hands".

## Build

```
cd paper
pdflatex dpe && bibtex dpe && pdflatex dpe && pdflatex dpe
```

MiKTeX on Windows lives at
`C:\Users\abptl\AppData\Local\Programs\MiKTeX\miktex\bin\x64`. The build is clean, with no
undefined references or citations. 19 pages.

## Why this repository exists

The paper had no source. The only artifact was a PDF built on 2026-09-08, which meant no
correction could be applied to it, and two corrections were already owed. Section 7 said
the Geometric Evaluation Theory campaign had not run when four of its questions had, and
the paper cited no classical work on invariance and objectivity while making that its
thesis. `PROVENANCE.md` records the reconstruction honestly, including the one symbol that
could not be recovered from the PDF and was restored by judgment.

## The record repositories

Every number in Sections 7 and 10 is read from a sealed record. The paper is a
methodological synthesis and owns no measurements of its own. Note that the Section 10
records are in a repository that is currently private, which the paper states.

| Section | Records |
|---|---|
| 7, Geometric Evaluation Theory | [`ahb-sjsu/geometric-evaluation-theory`](https://github.com/ahb-sjsu/geometric-evaluation-theory), gates G2, G3, G4, G4b, G5 |
| 10, nine registrations and one law | `ahb-sjsu/observation-theory-campaigns` (**private**), OD track gates D2 through D2v9 |
| 8, economic stake invariance | IEEE TCSS, accepted 2026-09-06, with `eris-econ` as the reference code |
| Throughout | [`ahb-sjsu/philosophy-engineering`](https://github.com/ahb-sjsu/philosophy-engineering), the discipline's specifications |

The four record types the paper's protocol needs exist as machine-readable records in the
campaigns repository, which are the transformation registry
(`claims/transformations/*.toml`), the per-entry invariance envelope, and the ledger
classes `[witness]` and `[revised]`. `standards/DPE-RECORDS.md` there states the protocol
steps they enforce and maps each to a definition in this paper. The corresponding
specification in the discipline's own repository is `spec/PE-DSC-1.0.md`.

## State, 2026-09-11

Drafted and building. Not submitted anywhere, and no venue chosen.

Open items for the author:

1. Confirm the reconstructed codomain of the judgment map, `\mathcal{P}(Y)`, against what
   the lost original wrote. See `PROVENANCE.md` section 2.
2. Decide whether the heading scheme should lose its colons, which the standing prose
   standard would require and which was left alone as a structural choice.
3. Choose a venue. The paper is 19 pages, which fits a philosophy of science or methodology
   journal and no conference page limit currently in view.
4. Fill the TCSS volume, issue, and pages in `refs.bib` once they are assigned. The entry
   carries a `% verify vol/pages on final` mark, which must not be removed silently.
