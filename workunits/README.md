# Workunit checkpoints

This directory stores small resumable checkpoints for bounded repository workunits.

A checkpoint records the capability/workunit, phase, exact repository state, inherited evidence, mutations, verdict, remaining boundaries and the next permitted action. It is process/governance state, not a scientific evidence source.

Checkpoints do not override canonical theory, schema, evidence registers or code. They exist so a later chat can resume from a verified state boundary instead of reconstructing completed work.
