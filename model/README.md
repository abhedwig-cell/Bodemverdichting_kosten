# Formal model registers

This directory contains machine-readable registers that connect the narrative formal model to implementation and review.

## `equations.csv`

One row per formal equation, identity or rule that can affect project results.

Each row records:

- stable `equation_id`;
- expression and variables/units;
- domain of validity;
- null behaviour;
- theory/evidence basis;
- code and test locations where executable;
- explicit exclusions;
- current capability status.

A documented equation is not automatically a qualified physical parameterisation. For example, the pump-energy identity is mathematically/physically stable while current Tollebeek head and efficiency remain data-gated.

## `traceability.csv`

One row per reviewable capability. It links:

**theory / claims → conceptual object → formal rule → canonical datasets → implementation → tests → evidence/qualification**.

The register is intended to make broken links visible. It should not be used to hide uncertainty by assigning a mature status to a capability whose physical inputs remain unavailable.

## Update rule

Review a row when any referenced equation, dataset meaning, implementation path, evidence/claim or scientific dependency changes. The Markdown traceability document remains the colleague-facing explanation; this directory is the machine-readable review surface.
