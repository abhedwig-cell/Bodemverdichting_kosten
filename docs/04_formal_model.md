# 4. Formal model

This document is the home for canonical equations, variable definitions, units and formal decision rules.

## 4.1 Paired attribution

For a response quantity `Y` under the same event and controlled context:

`delta_Y = Y_current - Y_reference`

The paired runs should differ only in the soil-state dimensions admitted for attribution.

## 4.2 Generated runoff volume

For affected area `A_ha` and extra generated runoff depth `delta_R_mm`:

`V_generated_m3 = 10 * A_ha * delta_R_mm`

This is generated parcel runoff and not automatically field-edge, ditch or pump volume.

## 4.3 Event-conditioned transfer

Occurrence and positive magnitude are separated conceptually:

- `P(R_edge > 0 | state, event, process, connectivity)`
- `V_edge | R_edge > 0`

A diagnostic event delivery ratio may be defined as:

`f_delivery_event = V_edge / V_generated`

but it is not a universal static project parameter.

## 4.4 Managed-system routing

Managed systems require explicit routing and allocation. For Tollebeek, current architecture distinguishes an IJsvogel core and a Kievit zone, with a one-way evidenced extreme assist route from Kievit-zone water to IJsvogel. The assist fraction has no default.

## 4.5 Pump energy

For pumped volume `V`, total dynamic head `H` and efficiency `eta`:

`E_kWh = rho * g * H * V / (eta * 3.6e6)`

Nominal target-level differences must not silently substitute for total dynamic head.

## 4.6 Cost

A direct pumping budget cost may combine:

`C_pump = E_kWh * p_electricity + attributable_variable_OM`

Budget expenditure, private cost and societal welfare effect remain separate valuation categories.

## 4.7 Formal status

The equations above are architecture-level relations. Numerical defaults are only canonical when separately supported and admitted in the evidence/qualification layer.
