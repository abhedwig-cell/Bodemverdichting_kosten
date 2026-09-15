# Source code

Scientific and data-processing code will be migrated here progressively.

Planned separation:

- `hydrology/` — source-response and hydrological calculations/adapters
- `transfer/` — event-conditioned source-to-receptor transfer
- `water_system/` — routing, pump dispatch, capacity and energy
- `valuation/` — explicit valuation relations and cost categories
- `io/` — data/workbook/application adapters

Do not duplicate scientific equations independently in multiple interfaces when a shared tested implementation is possible.
