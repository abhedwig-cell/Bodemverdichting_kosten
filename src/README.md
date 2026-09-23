# Source code

`src/` contains shared scientific calculations whose meaning should not depend on Excel, a dashboard or a future application.

## Currently implemented

- `transfer/volume.py`: generated source-volume identity;
- `water_system/dispatch.py`: explicit two-zone/two-pump allocation semantics without hidden assist or availability defaults;
- `water_system/energy.py`: pump-energy identity with explicit total dynamic head and efficiency.

These implementations are generic even though the first qualification case was Tollebeek. Site-specific values belong in qualified data/configuration, not in scientific core functions.

## Intended future separation

Additional packages such as hydrology/source-response adapters, valuation and I/O may be added when real workflows require them. They are architectural directions, not directories that are assumed to exist today.

Do not create empty package structure merely to mirror a diagram. Add a module only when a formal relation or reusable data-processing responsibility has a concrete implementation and test.

The current vertical-slice history is documented in [`docs/11_tollebeek_vertical_slice_v0_2.md`](../docs/11_tollebeek_vertical_slice_v0_2.md). The current project-wide architecture/readiness is in [`PROJECT_ARCHITECTURE_STATUS.md`](../PROJECT_ARCHITECTURE_STATUS.md).

Do not duplicate scientific equations independently in multiple interfaces when a shared tested implementation is possible.