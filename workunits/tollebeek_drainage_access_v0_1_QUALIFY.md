# Tollebeek drainage access v0.1 — QUALIFY

Capability: `DR_SM_DRAINAGE`

Phase: `QUALIFY`

Canonical start:
- `main = a02e0810e2a1bfd9d4d8c5c5f418a012c8d55206`

Qualified PR postimage before this checkpoint:
- branch head: `6c625fb461aed2265d2db868ca61407c0c20859b`
- PR: `#37`
- CI: `35081269168 = SUCCESS`

Qualified decision:
- ordinary Waterschap Zuiderzeeland water-information request is the primary owner route for missing drainage detail;
- technical/data-holder clarification follows if the public `zzl_Drainage` fields are incomplete/placeholder exports;
- Woo route is secondary escalation only if formal disclosure is required;
- requested payload is source-native OT.02 drainage geometry/table detail plus field definitions, temporal/version metadata and missing-value semantics.

Scientific boundary:
- `DR_SM_DRAINAGE` remains `PARTIAL_EVIDENCE`;
- `CAP_MULTI_DRAIN` remains data-gated;
- no spacing, depth, installation date, resistance or SWAP drainage configuration is admitted;
- spacing `0` remains missing/sentinel-like;
- FutureWater 100 d / ~30 d remain method priors only.

Diff class:
- documentation/governance only;
- no schema, evidence-register, readiness-register, numerical input or model implementation mutation.

Verdict:
`QUALIFIED_ZZL_SOURCE_HOLDER_ACCESS_ROUTE_PHYSICAL_ATTRIBUTES_PENDING`

Next permitted action:
- require CI success on this exact checkpoint head;
- merge only from that head if canonical dependencies remain unchanged;
- after merge, request owner records and open a separate bounded qualification workunit only upon receipt.
