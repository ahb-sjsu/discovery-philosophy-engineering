# Provenance of `paper/dpe.tex`

The original LaTeX source for this paper does not exist. The only artifact was
`Discovery_Philosophy_Engineering.pdf`, built 2026-09-08 09:33 PDT with pdfTeX 1.40.26,
15 pages, letter, Latin Modern. This file records exactly what in the reconstructed source
is the author's 2026-09-08 text, what was restored by judgment, and what is new on
2026-09-11. Read it before treating any sentence as the author's original wording.

## 1. Carried over from the 2026-09-08 PDF

The argument, the section order, the five theorem-like statements (Principle 1,
Definitions 1 to 4, Proposition 1 with its proof, Remark 1, Conjecture 1), the probe ladder
table of Section 4.5, the loop figure, Sections 1 to 6, 8, 9, and 11 to 16, and the
thirteen original references. The claims are the author's and were not changed.

## 2. Restored by judgment, and open for the author to correct

- **The codomain of the judgment map.** The PDF renders the display as `J : X → (Y)` with
  the symbol before `(Y)` lost to text extraction. It is reconstructed as
  `\mathcal{P}(Y)`, described in the text as the space of distributions over `Y`, which is
  what the draft's own next sentence requires when it says deterministic judgments are
  included as degenerate distributions. If the original was `Δ(Y)`, change one macro.
- **Document class and geometry.** `article`, 11pt, letter, 1in margins, Latin Modern,
  `natbib` with `plainnat`. This reproduces the PDF's typography and is not claimed to be
  the original preamble.
- **Figure 1** is redrawn in TikZ from the node text and the six-node cycle the PDF shows.
  The original drawing package is unknown.

## 3. Changed on 2026-09-11

### 3.1 Section 7 replaced, because the draft's version was false

The 2026-09-08 Section 7 said of the GET repository that it "states that its empirical
campaign has not yet run" and asked that GET "be treated here as a formal research program,
not as an established measured theory." That was true when written and is not true now.
Section 7 is replaced with text written from the sealed campaign records of
`ahb-sjsu/geometric-evaluation-theory`. Every number in it is read from a record, cited
below.

| Statement | Record |
|---|---|
| Hull law, 489 testable, 50 percent violate, 66 percent under shuffles, 0 of 200, five replication pairs | `experiments/G2/results.json`, `CAMPAIGN.md` G2, sealed `PREREG-G2.md` blob `fd7cc924` |
| Threshold tracks budget, 0.87 to 0.88 of every predicted step, largest ratio 1.15 against tolerance 1.5, weight precision does not move it, two discarded chooser instruments | `experiments/G3/results.json`, `grade.json`, `CAMPAIGN.md` G3, sealed `PREREG-G3.md` blob `53cb1a00` |
| Shared code first run, 20 to 330 times the prediction, 32 of 32 ordering | `experiments/G4/results.json`, `CAMPAIGN.md` G4, sealed `PREREG-G4.md` blob `91c834f7` |
| Shared code second run, ratio 1.02 to 1.05, flat to a tenth of a whitened unit, 20 percent scatter, seed check | `experiments/G4b/results.json`, `seedcheck.json`, `CAMPAIGN.md` G4b, sealed `PREREG-G4B.md` blob `d6d1c44f` |
| Identification, two pilots, bars restated relative to chance, PASS 12 of 12 | `experiments/G5/PREREG-G5.md` blob `66dbc686`, `pilot.json`, `grade.json`, `CAMPAIGN.md` G5 |

The base text came from `geometric-evaluation-theory/articles/2026-09-08-dpe-section7-get-under-its-own-campaign.md`,
which was itself written at GET commit `325faee` and covered three gates. The G3 paragraph
is new on 2026-09-11, because G3 was sealed and run on 2026-09-09, after that article was
written. The opening count was corrected from three gates to four questions across five
sealed registrations.

### 3.2 Section 10 is new

"Worked Example V: Nine registrations and one law" is written from
`ahb-sjsu/observation-theory-campaigns`, article
`articles/2026-09-10-nine-registrations-one-law.md` and the records it cites, which are
`experiments/DISCOVERY-TRACK.md` gates D2 through D2v9, `experiments/OD/D2v7/law.json`,
`experiments/OD/D2v9/{law.json,grade.json}`, `experiments/OD/D2v9_explore/README.md`,
`experiments/OD/D2_close/`, and the registry tests in `claims/transformations/OD.toml`.
None of that existed on 2026-09-08. Every number in the section is read from those records
and nothing in it is a new claim.

It is included because it is the only case on record in which the Section 4 protocol ran to
its own declared end, and because three of its nine registrations failed, which the other
four worked examples do not show.

### 3.3 Six references added

All six were verified against publisher or indexing records on 2026-09-11.

| Key | Why it was added |
|---|---|
| `klein1893` | The Erlangen reading of geometry as what a transformation group fixes. The draft asserted this history without a citation. |
| `weyl1952` | Its extension to physical law, same sentence. |
| `nozick2001` | *Invariances* is the closest prior statement of the paper's own thesis inside philosophy, and the draft did not cite it. This was the most serious omission. |
| `vanfraassen1989` | *Laws and Symmetry* is the standard form of Section 14.2's objection, now answered rather than only conceded. |
| `mayo2018` | Severe testing is the notion Section 4 uses when it says "increasingly severe", now defined at first use. |
| `zeller2002` | Delta debugging is the same reduction move as Definition 4, cited at Definition 4 and at Section 14.1, where the draft already said the method is "closer to debugging". |

### 3.4 Acknowledgment corrected, and AI use disclosed

The old acknowledgment ended "unrun GET campaign gates are not presented as measured
results", which no longer describes the paper. It now states that every number in Sections
7 and 10 is read from a sealed record. An AI-use disclosure was added, per the presentation
standard.

### 3.5 Prose edited to the standing house standard

The body prose was edited to remove em-dashes, colons, and semicolons, and the displayed
arrow chains in the introduction and conclusion were written out as prose, because the
standard forbids mathematics in the abstract and introduction. Equation numbering therefore
differs from the 2026-09-08 PDF. The original had eleven numbered equations and this source
has seven, the four dropped ones being the arrow chains, which carried no mathematics.

**Not done.** The section headings still use the author's "Worked Example I:" and
"Workstream A:" scheme, which the standard's clause on colons in headings would change.
That is a structural naming decision for the author, not an editing one, and it was left
alone.

## 4. Build

```
cd paper
pdflatex dpe && bibtex dpe && pdflatex dpe && pdflatex dpe
```

Builds clean on MiKTeX with no undefined references or citations. 19 pages as of
2026-09-11, against 15 for the 2026-09-08 original.
