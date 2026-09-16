# Formal equation and traceability register v0.1

Status: **working baseline**

Purpose: convert the most important parts of the Status-A-light formal model and cross-layer traceability from narrative-only documentation into machine-readable registers that can be validated and later exposed in generated artifacts or the application.

## 1. Why this exists

The repository already documents the chain:

**theory → conceptual model → formal model → data model → implementation → evidence/qualification → artifact/application**.

The Markdown traceability matrix is intentionally readable for colleagues, but a Status-A-like project also needs stable identifiers and integrity checks so that equation, code and evidence references cannot silently drift.

This baseline therefore adds:

- `model/equations.csv` — formal equations, identities and rules;
- `model/traceability.csv` — capability-level cross-layer links;
- `schema/formal_traceability_fields.yml` — field semantics;
- `tools/validate_formal_traceability.py` — integrity checks;
- `tests/test_formal_traceability.py` — regression tests for the register and key data gates.

## 2. Equation register

The first equation set contains the currently important executable or near-executable relations:

- matched current/reference attribution;
- generated runoff-volume conversion;
- event delivery diagnostic;
- assist allocation;
- available pump capacity;
- pump hours;
- response-window capacity pressure;
- pump energy;
- direct pumping budget cost.

Each equation records not just an expression but also domain of validity, null behaviour, theory/evidence basis, code location, test location and prohibited shortcuts.

This is important because an equation can be stable while its inputs remain scientifically unqualified. For example, the pump-energy identity is executable and tested, while current Tollebeek head and efficiency remain data-gated.

## 3. Traceability register

`model/traceability.csv` mirrors the major capabilities in `15_traceability_matrix_v0_1.md` but uses stable identifiers and explicit references.

The register links each capability to, where available:

- theory or qualified claims;
- conceptual objects;
- formal equation IDs;
- canonical dataset IDs;
- code paths;
- tests;
- evidence/claim IDs;
- current maturity/data-gate status;
- the current broken link;
- review triggers.

The register is not an attempt to duplicate all documentation. It is a machine-readable control surface for detecting broken links.

## 4. Current scientific boundary

This step does **not** advance the physical Tollebeek result.

The main data gates remain unchanged:

1. current/reference source attribution needs current depth-resolved soil/drainage state;
2. field-edge/system transfer needs event-conditioned empirical qualification;
3. Kievit/IJsvogel operation needs current pump, routing, availability, head and efficiency evidence;
4. current direct cost needs current tariffs and attributable variable O&M after physical attribution is complete.

The new registers make these gaps more explicit; they do not fill them.

## 5. Validation

The validator checks at least:

- unique equation and capability IDs;
- controlled capability-status values;
- equation references from traceability rows;
- dataset IDs against `schema/datasets.yml`;
- claim/evidence IDs against the canonical evidence registers;
- repository code and test paths where declared.

A passing integrity test means the documentation/data/code references are internally connected. It does not qualify a physical model result.

## 6. Next use

The next useful extension is to let the generated colleague workbook expose `model/equations.csv` and `model/traceability.csv` as read-only review datasets. That would complete a first end-to-end documentation artifact in which colleagues can move from theory and claims to equations, data objects, implementation and current scientific gaps without reading legacy workbook sheets.
