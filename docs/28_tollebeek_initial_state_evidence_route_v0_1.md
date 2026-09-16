# Tollebeek 1998 initial-state evidence route v0.1

Status: **ROUTE QUALIFIED, INITIAL STATE NOT ADMITTED**

## Decision

The October 1998 event now has a qualified public historical-groundwater acquisition route, but the project does **not** have an admitted hydrological initial state for OT.02. `DR_SM_INITIAL_STATE` therefore advances from `MISSING` to `PARTIAL_EVIDENCE`, not to `ADMITTED`.

## Evidence resolved

Two BRO GLD series are located inside the admitted OT.02 polygon at well `GMW000000053815` (`B20F0038`, RD 173300/522600, registered ground NAP -4.58 m). Their nearest pre-event observations on 14 October 1998 are about NAP -4.93 and -4.88 m. The monitoring screens, however, are deep: about NAP -16.3 to -17.3 m and -41.8 to -42.8 m. These are piezometric-head anchors, not direct phreatic/root-zone observations, and the historical observations are classified `onbekend`.

A systematic screening of historical GLD series within 10 km whose registered period covers 24 October 1998 and whose screen top lies 0-5 m below registered ground found four shallow candidates and **zero inside OT.02**. The closest shallow candidate is about 1.08 km outside OT.02 and is measured 6.4 days after the event start. All four shallow historical candidate series have status/class `onbekend`.

## Owner wetness context

The existing owner narrative that rain had fallen for days and that the ground was fully saturated remains useful event context. It is not converted into a numerical water-content, pressure-head or groundwater profile.

## What is not permitted

- deep piezometric head → phreatic groundwater table;
- target peil NAP -6.20 m → initial groundwater level;
- `fully saturated` narrative → numerical saturation or pressure-head profile;
- spatial interpolation from the outside shallow candidates into OT.02;
- field-capacity, hydrostatic or other convenience defaults;
- warm-up/restart before its required forcing, model, boundary, drainage and land-use dependencies are explicitly qualified.

## Next route

First seek owner/DINO/BRO archival shallow groundwater or soil-water observations inside or directly representative of OT.02 around 24 October 1998, preserving coordinates/CRS, datum, screen/depth, measurement time and QC. If no suitable observation can be recovered, a warm-up/restart decision becomes reviewable only after the remaining controlled model inputs are admitted.
