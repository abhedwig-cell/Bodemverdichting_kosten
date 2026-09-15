# Evidence registers

The evidence directory is the canonical, machine-readable evidence layer for the project.

The intended chain is:

`source -> evidence item -> claim -> qualification -> project use`

Files:

- `sources.csv`: one row per source/version;
- `evidence_register.csv`: one row per extractable fact, measurement or relation;
- `claims.csv`: project interpretations that may combine or constrain multiple evidence items;
- `qualification_register.csv`: intended-use qualification of evidence items.

## Rules

1. A source is not automatically a model parameter.
2. Evidence status and qualification verdict are different concepts.
3. A historical benchmark remains historical unless separately qualified for transfer.
4. Unknown or unavailable values remain blank/null; they are never silently turned into zero.
5. A qualified value can still carry a guardrail that restricts how it may be used.
6. Legacy workbook tables are migration sources. They do not override the canonical evidence register.

Run:

```bash
python tools/validate_evidence.py
```

to check identifiers, foreign keys and controlled-vocabulary values.
