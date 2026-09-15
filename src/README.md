# Source code

Scientific and data-processing code is migrated here progressively.

Current separation:

- `hydrology/` — source-response and hydrological calculations/adapters
- `transfer/` — event-conditioned source-to-receptor transfer
- `water_system/` — routing, pump dispatch, capacity and energy
- `valuation/` — explicit valuation relations and cost categories
- `io/` — data/workbook/application adapters

The first implemented vertical slice is documented in
[`docs/11_tollebeek_vertical_slice_v0_2.md`](../docs/11_tollebeek_vertical_slice_v0_2.md).

Current code in that slice is deliberately generic:

- `transfer/volume.py` implements the generated-volume identity;
- `water_system/dispatch.py` implements explicit two-zone/two-pump allocation without hidden operational defaults;
- `water_system/energy.py` implements the pump-energy identity with explicit head and efficiency.

Do not duplicate scientific equations independently in multiple interfaces when a shared tested implementation is possible.
