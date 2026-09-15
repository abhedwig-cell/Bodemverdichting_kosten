# 11. Tollebeek vertical slice v0.2

## Purpose

This is the first end-to-end implementation slice used to test whether the Status-A-light architecture works across:

**formal relation → data meaning → code → software tests → evidence/qualification boundary**

The slice is intentionally narrow:

**generated source response → transfer-stage volume → two-pump dispatch → pump energy identity**

It does not create new Tollebeek hydrology or operational evidence.

## Scientific boundary

The slice begins only after a current/reference source response has been qualified.

For a matched pair of runs:

`V_generated = 10 × A_affected × ΔR`

where area is in ha and runoff difference in mm/event.

That generated parcel volume is not automatically field-edge, ditch, network or pumped volume.

The transfer layer must keep these stages separate.

## Dispatch semantics

The implementation uses a generic two-zone/two-pump topology:

- a primary source zone routes to a primary pump;
- a second source zone routes to its own pump;
- an explicit fraction of the second zone may be assisted by the primary pump;
- no reverse-assist route is modelled unless evidence supports it.

This matches the current Tollebeek conceptual topology without hard-coding asset names or capacities in code.

Capacity and assist inputs are supplied explicitly.

There is deliberately no hidden default for:

- assist fraction;
- capacity availability;
- total dynamic head;
- pump efficiency;
- response window.

## Energy identity

Where pumped volume, total dynamic head and efficiency are known:

`E_kWh = rho × g × H × V / (eta × 3.6e6)`

Head and efficiency stay null until qualified operating-point evidence is available.

## Null semantics

Unknown values remain `None`/null.

The code does not convert unknown values to zero.

This is a scientific requirement, not merely a programming preference.

## Implementation

Current modules:

- `src/transfer/volume.py`
- `src/water_system/dispatch.py`
- `src/water_system/energy.py`

Schema support:

- `schema/relationships.yml`
- `schema/tollebeek_vertical_slice.yml`

Software qualification:

- `tests/test_vertical_slice.py`

## Test status

Tests are software QA only. They verify:

- the unit identity for generated volume;
- null propagation;
- absence of a hidden assist default;
- explicit assist allocation;
- fraction validation;
- pump-energy identity;
- no hidden head or efficiency defaults.

Synthetic numerical fixtures in tests are not Tollebeek scientific scenarios.

## What remains scientifically blocked

The implementation is ready to consume data, but the following remain external scientific/data gates:

- qualified current/reference SWAP source response;
- field-edge / ditch / network transfer;
- current OT.02 routing geometry;
- event-specific assist/control rule;
- current De Kievit operating curve;
- event-specific pump availability;
- pump-specific total dynamic head and efficiency/energy telemetry.

Therefore this workunit qualifies architecture and software semantics, not the physical Tollebeek result.
