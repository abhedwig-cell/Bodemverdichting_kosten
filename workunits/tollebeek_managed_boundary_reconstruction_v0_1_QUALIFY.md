# Tollebeek managed-boundary reconstruction v0.1 — QUALIFY checkpoint

Date: 2026-09-16
Protocol phase: QUALIFY

## Authority

- canonical start: `main` @ `a8b62c423391bf13ff8e638a749d70f4c9ab6944`
- branch pre-checkpoint qualified head: `b3a812bcddd65d351ddde65bd627f95ceffd1528`
- pull request: `#30`
- PR-head CI: `35076564536` — SUCCESS

## Qualified verdict

`MANAGED_BOUNDARY_RECONSTRUCTION_PROTOCOL_QUALIFIED_NO_EVENT_BOUNDARY_ADMISSION`

The protocol defines four evidence/reconstruction levels:

- `R0 OBSERVED_EVENT_BOUNDARY`
- `R1 CONSTRAINED_HISTORICAL_RECONSTRUCTION`
- `R2 ENVELOPE_ONLY_SCENARIO`
- `R3 INADMISSIBLE_DEFAULT`

## Preserved scientific boundaries

- NAP -6.20 m remains a target level, not an event hydrograph.
- Nominal pump capacity remains distinct from realized operation/discharge.
- 2006 near-period capacities are not silently transferred to exact 1998 values.
- Emergency pumping is a required historical constraint, not an optional detail.
- Post-1998 IJsvogel/current merged OT.02 controls remain excluded from silent backcast.
- Non-identifiability must be represented through alternatives/ranges rather than one hidden best guess.
- The same boundary reconstruction/member must be used for CURRENT and REFERENCE in simple soil-state attribution.

## Mutations

Documentation/governance only. No numerical boundary, model-input dataset, evidence verdict, readiness status, schema or model output is changed.

`DR_SM_MANAGED_BOUNDARY` remains `PARTIAL_EVIDENCE`.

## Tests

PR-head `b3a812bcddd65d351ddde65bd627f95ceffd1528`:

- CI run `35076564536`: SUCCESS
- compile gate: PASS
- Status-A-light integrity gate: PASS
- full unit/contract suite: PASS

## Next permitted action

After exact-head CI, merge the protocol only. A future numerical R1/R2 reconstruction is a separate scientific workunit and requires either new archive evidence or explicit bounded free-parameter/uncertainty construction according to this protocol.

No model run is authorized here.