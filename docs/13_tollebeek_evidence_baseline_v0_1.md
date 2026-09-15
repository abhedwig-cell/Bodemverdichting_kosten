# Tollebeek evidence baseline v0.1

Status: **migration baseline / Status-A-light**

This document records the first canonical evidence slice for the Tollebeek line. It is intentionally narrower than the full workbook history. The purpose is to show how public and technical sources become project evidence, how that evidence is qualified for specific uses, and where the chain remains blocked.

## 1. Evidence architecture

The project separates four things that legacy workbooks often mixed together:

1. **Source** — a report, dataset, service or administrative publication.
2. **Evidence item** — one extractable fact or relation from that source.
3. **Claim** — the project interpretation that combines or constrains evidence.
4. **Qualification** — whether the evidence/claim supports one specific intended project use.

A value is therefore not accepted merely because it exists in a source. The intended use and its guardrail are part of the scientific record.

## 2. Administrative area and boundary

The 2010 peilbesluit merged the former Rietgors (762 ha), Fuut (367 ha) and Kievit (373 ha) areas into a new OT.02 of 1502 ha. A later official overview reports OT.02 at 1497 ha.

Project interpretation:

- **1497 ha** is used as the administrative system-area benchmark until a reviewed current geometry supersedes it;
- **1502 ha** remains the 2010 design-area context and is useful for historical stratification;
- neither number is an estimate of the area affected by soil compaction.

The current peilgebied geometry remains a data gate. PDOK IMWA is the preferred public discovery route, but one feature must still be explicitly reviewed and admitted before spatial soil sampling.

## 3. Managed hydrological setting

OT.02 has a managed target surface-water level of NAP -6.20 m and a coupled underdrainage system. This supports a managed-boundary representation in the Tollebeek SWAP work and argues against using free drainage as the default lower-boundary concept.

This does **not** yet define the event-specific groundwater state, current control logic or the total dynamic head of either pump.

## 4. Pump assets and topology

### IJsvogel

The owner-backed public source gives a combined installed capacity of **540 m3/min** for three large screw pumps. A separate regional description gives **9 m3/s**, which is the same value after unit conversion.

Project claim:

> 540 m3/min is the admitted IJsvogel installed-capacity benchmark.

Guardrail:

> installed capacity is not the same as event-specific available incremental capacity and is not automatically the effective capacity of the complete OT.02 system.

### Kievit

The evidence describes different quantities:

- nominal hardware description: **2 x 30 m3/min at 1.40 m head**;
- historical calculated capacity in the 2010 peilbesluit: **1.44 m3/s**;
- a public description also records a material renovation in 2020.

Project interpretation:

> current effective Kievit operating capacity is still unknown.

The 60 m3/min and 1.44 m3/s values are deliberately not converted into a min/max range because they may represent different definitions and operating assumptions.

## 5. Pump dispatch

The Kievit and IJsvogel underdrainage areas are coupled. Public system evidence states that, under extreme conditions, IJsvogel can discharge part of the water from the Kievit area.

This supports the directional dispatch semantics already implemented in code:

- IJsvogel-core water -> IJsvogel primary;
- Kievit-zone water -> Kievit primary;
- Kievit-zone water -> IJsvogel assist under an explicitly defined operating state.

No universal assist fraction is admitted. Reverse routing from the IJsvogel core to Kievit is not currently evidenced.

## 6. Historical SWAP priors

FutureWater Report 50 is retained as a historical regional method source. It supports the structural use of managed surface-water levels, spatial seepage and multiple drainage systems in a Noordoostpolder SWAP setup.

Historical numerical settings such as a **100 d tile-drain resistance** and an approximately **30 d surface-drainage resistance** are qualified only as method/sensitivity priors. They are not current OT.02 calibration values.

## 7. Soil profile route

WUR Soil Physical Data and BOFEK2020 provide the preferred route to a reproducible profile ensemble once the current OT.02 sampling domain is admitted.

The key semantic boundary remains:

- derived/modal profile != direct soil measurement;
- API bulk density != automatically the current compaction state;
- one convenient coordinate != representative Tollebeek profile.

## 8. Current qualification boundary

The following are currently qualified for architectural/model use:

- 1497-ha administrative area benchmark with limitations;
- NAP -6.20 m managed-level context;
- IJsvogel 540 m3/min installed benchmark;
- coupled Kievit/IJsvogel topology;
- directional Kievit-zone -> IJsvogel assist semantics;
- historical NOP drainage settings as bounded method priors.

The following remain blocked or explicitly unknown:

- reviewed current OT.02 geometry;
- current spatial drainage configuration;
- current depth-resolved compaction state and matched reference state;
- current post-2020 Kievit Q-H/Q-eta operating curve;
- event-specific assist fraction and conveyance capacity;
- pump-specific current head, efficiency and energy intensity;
- attributable hydrological delta from paired current/reference SWAP runs.

## 9. Canonical files

- `evidence/sources.csv`
- `evidence/evidence_register.csv`
- `evidence/claims.csv`
- `evidence/qualification_register.csv`

These files are the first canonical evidence baseline for the Tollebeek vertical slice. Legacy workbook tables remain useful as migration sources but do not override this qualification structure.
