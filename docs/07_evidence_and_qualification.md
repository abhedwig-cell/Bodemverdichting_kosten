# 7. Evidence and qualification

## Principle

A source citation, an observed value, a model input and an admitted project parameter are different states.

## Suggested chain

`Source → EvidenceItem → Claim → Qualification → AdmissionDecision`

## Evidence classes

Examples include:

- direct measurement;
- derived measurement;
- official administrative/system metadata;
- model output;
- peer-reviewed relation;
- historical benchmark;
- scenario assumption;
- software QA evidence.

## Qualification questions

For important evidence ask:

1. What exactly was measured or derived?
2. For which population, location, time and scale?
3. What model quantity may it support?
4. Which dependencies affect validity?
5. Is independent qualification available?
6. What use is explicitly prohibited?

## Admission examples

Possible statuses include `ADMITTED`, `BENCHMARK_ONLY`, `SCENARIO_ONLY`, `METHOD_PRIOR`, `CONTEXT_ONLY`, `WAIT_DATA`, `BLOCKED` and `REJECTED_FOR_PROJECT_USE`.

## Evidence inheritance

Immutable evidence may be reused when the relevant scientific and data dependencies have not changed. A new workbook version by itself does not invalidate evidence.

## Current registers

Bootstrap CSV registers live under [`../evidence/`](../evidence/). They are intentionally sparse until the existing evidence inventory is migrated and reconciled.
