# Tollebeek initial state v0.1 — execution note

Date: 2026-09-16
Capability: `DR_SM_INITIAL_STATE`

This note records tooling-only failures after the scientific ACQUIRE/REVIEW decision was already established.

- Run `35071385752`: the generated route postimage was not committed because the temporary finalizer environment lacked `PyYAML`, which is required by the existing central project validator.
- Run `35071474635`: after installing `PyYAML`, the generated postimage passed the central Status-A-light project validator and the complete test suite (`33/33` tests). The subsequent bot push was rejected only because the same commit also modified `.github/workflows/ci.yml` and the Actions token lacks `workflows` permission.
- No scientific value, initial groundwater level, pressure-head profile, water-content profile, warm-up state or restart state was admitted by either failed attempt.
- Recovery rule: persist the already validated scientific postimage without workflow files; update the CI workflow separately through an authorized GitHub connector mutation; then qualify the clean exact head.

This is an execution/governance note, not additional scientific evidence.
