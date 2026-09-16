# Tollebeek 1998 initial-state data request v0.1

Purpose: resolve `DR_SM_INITIAL_STATE` for event `EVT_TOL_1998_OCT` without convenience defaults.

Preferred evidence is a shallow/phreatic groundwater or soil-water observation inside or demonstrably representative of admitted OT.02 near `1998-10-24T00:00:00Z`. Required metadata include stable observation/well ID, coordinates and CRS, measurement date/time and timezone, vertical datum, local ground elevation, screen/depth interval, source-native value/unit, quality/assessment status and provenance.

Deep piezometric heads can be retained as hydrogeological context but require a separate relationship/representativeness argument before any use in a soil-profile initialization. Surface-water target peil is not a substitute.

If direct observation cannot be recovered, do not invent a state. A warm-up/restart alternative may be reviewed only after model authority/configuration, managed-boundary behaviour, drainage and land-use/crop context are sufficiently specified to reproduce the pre-event state. CURRENT and REFERENCE must receive identical or explicitly equivalent initialization semantics.
