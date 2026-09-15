# Workbook inventory

This folder contains the compact, machine-generated inventory summary used to prepare Data Model v0.2.

These files are **migration evidence**, not canonical scientific datasets.

Inspected artifacts:

- `FULL_SNAPSHOT_V3_8`: `Bodemverdichting_Cost_Framework_v3_8_TollebeekReconciled.xlsx`
- `MODULE_V4_4`: `Bodemverdichting_Cost_Framework_v4_4_CapacityReconciliation_DataRequest.xlsx`

The key structural finding is that v4.4 is a bounded module and not a cumulative replacement for the 109-sheet v3.8 full snapshot.

The full generated sheet and field inventories are retained as analysis artifacts outside the repository for now. They can be regenerated during migration. Observed workbook header names remain legacy aliases until explicitly reconciled with `schema/fields.yml`.
