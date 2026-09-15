# Workbook inventory

This folder contains machine-generated inventories of the prototype workbook lineage used to prepare Data Model v0.2.

These files are **migration evidence**, not canonical scientific datasets.

Inspected artifacts:

- `FULL_SNAPSHOT_V3_8`: `Bodemverdichting_Cost_Framework_v3_8_TollebeekReconciled.xlsx`
- `MODULE_V4_4`: `Bodemverdichting_Cost_Framework_v4_4_CapacityReconciliation_DataRequest.xlsx`

The key structural finding is that v4.4 is a bounded module and not a cumulative replacement for the 109-sheet v3.8 full snapshot.

`workbook_field_inventory_v0_2.csv` records observed workbook headers. Observed header names remain legacy aliases until explicitly reconciled with `schema/fields.yml`.
