# Tollebeek initial state v0.1 — ACQUIRE / REVIEW checkpoint

- canonical start: `96e0043196f1bacf7274e6071e46d9552421dd6c`
- branch: `work/tollebeek-initial-state-v0.1`
- fixed event: `EVT_TOL_1998_OCT`
- discovery run `35070705726`: SUCCESS; 51 historical GLD series within 10 km whose metadata span 1998-10-24; 2 inside OT.02
- discovery artifact digest: `7fa1b3c72d52f34d95532da808445559f2cddec55ca6a6fc64a4ce0041ba1273`
- source-form/metadata inspection run `35070914997`: historical compact CSV confirmed headerless; inside records are observation class `onbekend`
- event-anchor run `35071012126`: SUCCESS; inside well `GMW000000053815`; deep screen geometry and nearest 1998 observations resolved
- event-anchor artifact digest: `a78abb7baf58a0b1e3d923bd56e34c5fe72b2d75758b109f55842ea9599b1812`
- shallow screening run `35071098623`: SUCCESS; screen-top depth 0-5 m; 4 candidates within 10 km; 0 inside OT.02
- shallow-screening artifact digest: `afd44fe2b11aa2f6e18e1cddcecf78e7dff12898e1769dbcb3d8bfab696fea37`

Verdict: `QUALIFY_INITIAL_STATE_OBSERVATION_ROUTE_NO_ADMIT_STATE`.

No groundwater-level input, pressure-head profile, water-content profile, saturation profile, warm-up state or restart state is admitted.
