# On-site ensemble source migration v0.1

Status: **QUALIFICATION CANDIDATE**  
Parent: `docs/50_evidence_ensemble_protocol_v0_1.md`  
Scope: first canonical source/evidence migration for `ENS_O1_GRASS_SAND` and `ENS_O1_MAIZE_SAND`.

## 1. Purpose

Move the first on-site ensemble members out of legacy-workbook-only status without converting them into one universal crop-damage coefficient.

The migration follows:

```text
SOURCE IDENTITY
  → EVIDENCE STATEMENT
  → PROJECT CLAIM
  → INTENDED-USE QUALIFICATION
  → ENSEMBLE MEMBER
```

## 2. Sources recovered

### Alblas et al. 1994 — silage maize

J. Alblas, F. Wanink, J.J.H. van den Akker and H.M.G. van der Werf.  
*Impact of traffic-induced compaction of sandy soils on the yield of silage maize in The Netherlands.*  
Soil & Tillage Research 29, 157–165.  
DOI: `10.1016/0167-1987(94)90052-3`.

Recovered quantitative source semantics:

- four Dutch sandy-soil locations;
- experimental period 1983–1986;
- response depended on soil profile and weather;
- average reported yield reductions about 15% at 10 Mg axle load and 4% at 5 Mg;
- context maxima up to 38%;
- historical study estimate around 7% of total Dutch silage-maize production.

Important boundary: axle-load treatment is not equivalent to a current CC-NL severity class.

### Arts, Verwijs & Van Maanen 1994 — grass

*De invloed van berijding op de fysische bodemconditie van zandgrond en de gevolgen daarvan voor de grasproduktie.*  
IMAG-DLO report 94-5.  
WUR eDepot: `https://edepot.wur.nl/342704`.

Recovered original-result semantics:

- Oostwaardhoeve;
- initially loosened sandy soil;
- treatments 0, 4.5, 8.5 and 14.5 t with a purpose-built load frame;
- grass yield was highest at the 4.5 t treatment;
- beyond 4.5 t, yield declined with increasing load;
- the 0 t loose-soil treatment also yielded less than 4.5 t;
- the load effect was statistically significant.

This is primarily a **GUARDRAIL** against a universal monotonic negative grass-yield relation.

### Snijders et al. 1994 — grass

P.J.M. Snijders, F.A. Wopereis, H. Everts and A.P. Wouters.  
*Effect bodemverdichting op opbrengst en stikstofopname Engels raaigras op zandgrond.*  
PR Rapport 152.  
WUR eDepot: `https://edepot.wur.nl/22947`.

Recovered semantics:

- drought-sensitive sandy grassland at Cranendonck;
- first-cut yield after establishment was lower on compacted plots;
- later years showed significantly higher yield on loaded plots;
- improved moisture supply/capillary rise was identified as a plausible mechanism.

This source is also retained primarily as a **GUARDRAIL/context member**, not as a damage coefficient.

### Groenendijk et al. 2017 — soil-improvement scenarios

WER Rapport 2811 / STOWA 2017-020, DOI `10.18174/418283`.

Directly verified synthesis values:

- grass: 3–5% higher long-term average yield after removal of moderate compaction;
- grass: 17–23% higher yield in very dry years;
- silage maize: up to 2% higher long-term average yield;
- silage maize: 3–41% higher yield in dry years.

These are **inverse soil-improvement/model scenarios**. They are not automatically equal to damage caused by a specified current compaction state.

## 3. Canonical migration

New sources:

- `SRC_ALBLAS1994`
- `SRC_ARTS1994`
- `SRC_SNIJDERS1994`

New evidence:

- `EV_ALBLAS_MAIZE_AXLE_RESPONSE`
- `EV_ALBLAS_MAIZE_NATIONAL_ESTIMATE`
- `EV_ARTS_GRASS_NONMONOTONIC`
- `EV_SNIJDERS_GRASS_SIGN_CHANGE`
- `EV_GROEN_GRASS_YIELD_LONGTERM`
- `EV_GROEN_GRASS_YIELD_DRY`
- `EV_GROEN_MAIZE_YIELD_LONGTERM`
- `EV_GROEN_MAIZE_YIELD_DRY`

New interpretation claims:

- `CL_ONSITE_GRASS_SAND_CONTEXT`
- `CL_ONSITE_MAIZE_SAND_CONTEXT`

The ensemble register now references these canonical evidence IDs for the grass/sand and maize/sand ensembles.

## 4. Ensemble verdicts

### ENS_O1_GRASS_SAND

Verdict remains:

`SCENARIO_ENSEMBLE`

Reason:

- direct Dutch grass experiments show non-monotonic and sign-changing responses;
- soil-improvement simulations are inverse-response scenarios;
- dry-year effects are materially different from long-term-average effects.

No central grass-damage coefficient is admitted.

### ENS_O1_MAIZE_SAND

Verdict remains:

`SCENARIO_ENSEMBLE`

Reason:

- Alblas is direct Dutch field evidence but based on axle-load treatments;
- Groenendijk gives inverse soil-improvement scenarios;
- dry-year effects differ strongly from long-term averages;
- the historical 7% national estimate is retained as benchmark only.

No CC-NL severity coefficient or current national maize-loss coefficient is admitted.

## 5. Uncertainty structure retained

For both ensembles the project now keeps separate:

- treatment/state uncertainty;
- soil/profile dependence;
- weather dependence;
- comparator/reference semantics;
- within-source ranges;
- between-source differences;
- direct versus inverse evidence.

## 6. What was deliberately not done

No:

- averaging across sources;
- 5–30% generic workplan damage factor;
- conversion of axle load to CC-NL severity;
- reversal of soil-improvement benefits into direct damage coefficients;
- annualisation of dry-year ranges;
- monetisation yet;
- SWAP/WOFOST rerun.

## 7. Remaining source-quality limits

- The Alblas bibliographic record/DOI and quantitative abstract-level results are recovered and cross-checked, but the full article text has not yet been ingested.
- The Snijders original report identity is recovered; full text extraction remains incomplete, while its key response interpretation is corroborated by later WUR synthesis.
- Arts original report text is directly recoverable and is strong enough for the response-shape guardrail.

These limitations are preserved in source/evidence qualification statuses rather than hidden.

## 8. Next permitted action

After repository qualification, the next substantive step is not to calculate a national damage number.

It is to construct the first bounded **soil × crop × exposure** calculation surface:

1. choose one or two priority sandy-soil crop contexts;
2. bind a qualified exposure definition;
3. retain the scenario ensemble as the response dimension;
4. add crop-specific economic valuation;
5. propagate source/scenario uncertainty to a cost band.

Only if this band remains too wide for the intended use should additional modelling be considered.
