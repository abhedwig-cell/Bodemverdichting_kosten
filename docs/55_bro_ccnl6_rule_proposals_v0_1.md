# BRO → CC-NL6 mapping proposals v0.1

Status: **QUALIFIED PROPOSAL METHOD — INDIVIDUAL SOIL-UNIT MAPPINGS NOT ADMITTED**  
Parent workunit: `54_onsite_maize_soil_crosswalk_v0_1.md`

## 1. Purpose

The maize × soil crosswalk is intentionally fail-closed: every BRO `soil_unit_code` that occurs below a target maize parcel must have an explicitly reviewed CC-NL6 mapping before area aggregation is allowed.

Reviewing every code from scratch is unnecessary because the official BRO soil legend already identifies many code families unambiguously by soil material/class.

This workunit therefore adds a proposal layer:

```text
intersecting BRO codes
  → official-legend family rule
  → candidate CC-NL6 proposal
  → human/scientific review
  → explicit mapping row
  → QUALIFIED or still REVIEW_REQUIRED
```

The proposal layer reduces repetitive work. It does **not** change the admission rule.

## 2. Canonical files

Rules:

`config/bro_ccnl6_family_rules_v0_1.csv`

Proposal generator:

`tools/propose_bro_ccnl6_mapping.py`

Final reviewed mapping:

`config/bro_sgm_to_ccnl6_mapping_v0_1.csv`

The rule table and final mapping table have different meanings:

- rule table = deterministic review aid;
- mapping table = explicit soil-unit decision surface used by the overlay.

## 3. Families with deterministic proposals

The official BRO legend supports the following proposal classes.

| BRO family | Candidate CC-NL6 | Reason |
|---|---|---|
| V | V | peat soils |
| W | M | organic-mineral / moerige soils |
| H | ZO | humuspodzol soils in kalkloos sand |
| Y | ZO | moderpodzol soils in kalkloos sand |
| EZ | ZE | thick eerd soils with sandy esdek |
| EL | L | thick eerd soils with loamy esdek |
| EK | K | thick eerd soils with clay/sandy-clay esdek |
| Z | ZO | sandy soils, after EZ is matched first |
| M | K | marine clay family |
| R | K | river clay family |
| MO / RO | K | non-ripened marine/river clay-sandy-clay families |
| KR / KX / KT | K | old clay families |
| L | L | loam family |
| BL | L | loam-brik |
| BK | K | old clay-brik |
| BZ | ZO | sand-brik |

Leading lower-case modifiers in a soil-unit code do not change this family proposal. For example, `bEZ21` remains an EZ-family proposal.

Specific families have higher rule priority than generic parent prefixes. Thus `MO...` is matched before generic `M...`, and `BL/BK/BZ` before generic `B`.

## 4. Families that remain review-required

Some families are deliberately not converted automatically.

### S...A

These special calcareous, lutum-poor soils sit near a texture transition between sand and very light sandy clay. A family prefix alone is therefore insufficient for a defensible CC-NL6 choice.

### Old South-Limburg families

`MZ`, `MK`, `MA`, `FK`, `FG`, `KM`, `KK`, and `KS` can involve different parent materials or texture interpretations.

### Generic brik or unknown codes

Only the documented `BL`, `BK`, and `BZ` brik subfamilies receive deterministic proposals. A generic unresolved `B...` code remains review-required.

Any unrecognised code also remains `REVIEW_REQUIRED`.

## 5. Proposal is not admission

The proposal generator emits:

- `AUTO_PROPOSAL`; or
- `REVIEW_REQUIRED`.

There is deliberately no `AUTO_QUALIFIED` state.

An `AUTO_PROPOSAL` may be copied into the final mapping only after review has confirmed that:

- the actual soil-unit code belongs to the proposed family;
- no composite/association semantics invalidate the simple family rule;
- the corresponding CC-NL6 interpretation is defensible;
- the mapping basis is documented.

Only then may the row become:

`mapping_status = QUALIFIED`

The overlay builder ignores proposal status. It only accepts the separately reviewed final mapping.

## 6. Productive fail-closed workflow

The first overlay run is expected to fail while the mapping register is incomplete.

Instead of only printing an error, the builder now writes:

`data/derived/onsite_maize_soil_unmapped_codes_2025.csv`

containing the exact BRO codes encountered under definitive 2025 silage-maize parcels, plus their soil-classification descriptions.

That file becomes the input to:

```bash
python tools/propose_bro_ccnl6_mapping.py \
  --input data/derived/onsite_maize_soil_unmapped_codes_2025.csv \
  --output data/derived/onsite_maize_soil_mapping_proposals_2025.csv
```

The resulting proposal report is a review queue, not a production mapping.

## 7. Final mapping semantics

The canonical mapping table permits:

### QUALIFIED

A valid CC-NL6 class and explicit `mapping_basis` are mandatory.

### REVIEW_REQUIRED

The CC-NL6 class may remain blank.

This is important: an unresolved scientific classification should remain genuinely unresolved rather than being forced into a candidate class merely to satisfy schema validation.

### REJECTED

A code may be retained as rejected where it is unsuitable for the intended crosswalk. It remains unusable by the overlay.

The overlay proceeds only when **every intersecting code is QUALIFIED**.

## 8. Why not classify every BRO code in advance?

The project only needs codes that actually intersect target maize geometry.

The bounded workflow therefore follows:

```text
target crop first
  → encountered soil codes
  → proposals/review only for encountered codes
```

This minimizes effort and reduces the risk of maintaining an unnecessary national translation table whose unused edge cases have not been reviewed.

## 9. Integrity tests

The repository validates:

- unique family rule tokens;
- valid rule priorities and proposal statuses;
- valid candidate CC-NL6 classes;
- mandatory fallback `UNKNOWN`;
- representative deterministic mappings;
- representative ambiguous families remaining review-required;
- unresolved `REVIEW_REQUIRED` final mappings being allowed to have a blank class;
- such unresolved rows still blocking the overlay.

This is a software-integrity verdict for the workflow, not an admission of any yet-unreviewed soil code.

## 10. Current verdict

The BRO→CC-NL6 translation problem is now reduced from an open-ended manual task to a bounded review workflow.

Current state:

- official family semantics: **QUALIFIED FOR PROPOSAL GENERATION**;
- proposal generator: **IMPLEMENTED**;
- ambiguous-family guardrail: **QUALIFIED**;
- final mapping rows: **still data/review-gated**;
- automatic mapping admission: **PROHIBITED**;
- maize × soil area result: **NOT YET GENERATED**.

The next productive step is source materialization and a first fail-closed overlay run. That run will tell us which soil codes actually need review.
