# Evidence registers

The evidence directory is the canonical, machine-readable evidence layer for the project.

The intended chain is:

`source -> evidence item -> claim -> qualification -> project use`

Files:

- `sources.csv`: one row per source/version;
- `evidence_register.csv`: one row per extractable fact, measurement or relation;
- `claims.csv`: project interpretations that may combine or constrain multiple evidence items;
- `qualification_register.csv`: intended-use qualification of evidence items.

The registers currently contain two bounded baselines:

- the Tollebeek managed-system / pump-dispatch evidence baseline;
- the v0.1 general theory evidence baseline linking core project principles to Keller 2019, Graves 2015, Groenendijk 2017, Kuhlman 2010 and Romero-Ruiz 2026.

Readable indexes are available in `docs/13_tollebeek_evidence_baseline_v0_1.md` and `docs/16_theory_evidence_baseline_v0_1.md`.

## Rules

1. A source is not automatically a model parameter.
2. Evidence status and qualification verdict are different concepts.
3. A historical benchmark remains historical unless separately qualified for transfer.
4. Unknown or unavailable values remain blank/null; they are never silently turned into zero.
5. A qualified value can still carry a guardrail that restricts how it may be used.
6. Legacy workbook tables are migration sources. They do not override the canonical evidence register.
7. Source-derived fact and project interpretation are separate records where the interpretation materially affects modelling or valuation.
8. A theory principle may be well supported while its local numerical parameterization remains data-gated.

Run:

```bash
python tools/validate_evidence.py
```

to check identifiers, foreign keys and controlled-vocabulary values.


## Project-wide effect and ensemble registers

- `effect_pathway_matrix_v0_1.csv` is the machine-readable on-site/off-site continuation matrix.
- `evidence_ensemble_register_v0_1.csv` seeds conservative source ensembles. Legacy-workbook members remain explicitly marked `LEGACY_WORKBOOK_NOT_YET_CANONICAL` until migrated/qualified; their presence in the register does not admit them as current Dutch coefficients.
