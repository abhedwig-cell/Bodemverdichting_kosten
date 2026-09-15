"""Topology-aware pump dispatch calculations.

The functions are intentionally generic. Capacity, availability and assist fractions
must be supplied explicitly by the caller; no Tollebeek operational defaults are hidden
in the implementation.
"""

from __future__ import annotations

from dataclasses import dataclass


def _fraction(name: str, value: float | None) -> float | None:
    if value is None:
        return None
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must be in [0, 1]")
    return value


@dataclass(frozen=True)
class DispatchResult:
    primary_zone_volume_m3: float | None
    assist_zone_volume_to_primary_m3: float | None
    assist_zone_volume_to_secondary_m3: float | None
    primary_total_volume_m3: float | None
    primary_available_capacity_m3_min: float | None
    secondary_available_capacity_m3_min: float | None
    primary_pump_hours: float | None
    secondary_pump_hours: float | None
    primary_window_pressure: float | None
    secondary_window_pressure: float | None
    status: str


def two_zone_two_pump_dispatch(
    *,
    primary_zone_volume_m3: float | None,
    assist_zone_volume_m3: float | None,
    assist_fraction_to_primary: float | None,
    primary_installed_capacity_m3_min: float | None,
    secondary_installed_capacity_m3_min: float | None,
    primary_availability_fraction: float | None = None,
    secondary_availability_fraction: float | None = None,
    response_window_h: float | None = None,
) -> DispatchResult:
    """Allocate two routed source-zone volumes over a primary and secondary pump.

    Semantics mirror the Tollebeek topology pattern without hard-coding asset names:
    - primary-zone water routes to the primary pump;
    - assist-zone water routes to the secondary pump, with an explicit fraction
      optionally assisted by the primary pump;
    - reverse routing from the primary zone to the secondary pump is not represented.

    Inputs are already network/routing volumes. This function must not be fed raw
    parcel-generated runoff without the preceding transfer/routing qualification.
    """
    for name, value in (
        ("primary_zone_volume_m3", primary_zone_volume_m3),
        ("assist_zone_volume_m3", assist_zone_volume_m3),
        ("primary_installed_capacity_m3_min", primary_installed_capacity_m3_min),
        ("secondary_installed_capacity_m3_min", secondary_installed_capacity_m3_min),
        ("response_window_h", response_window_h),
    ):
        if value is not None and value < 0:
            raise ValueError(f"{name} must be >= 0")

    assist = _fraction("assist_fraction_to_primary", assist_fraction_to_primary)
    primary_avail = _fraction(
        "primary_availability_fraction", primary_availability_fraction
    )
    secondary_avail = _fraction(
        "secondary_availability_fraction", secondary_availability_fraction
    )

    if assist is None or primary_zone_volume_m3 is None or assist_zone_volume_m3 is None:
        return DispatchResult(
            primary_zone_volume_m3=primary_zone_volume_m3,
            assist_zone_volume_to_primary_m3=None,
            assist_zone_volume_to_secondary_m3=None,
            primary_total_volume_m3=None,
            primary_available_capacity_m3_min=None
            if primary_avail is None or primary_installed_capacity_m3_min is None
            else primary_installed_capacity_m3_min * primary_avail,
            secondary_available_capacity_m3_min=None
            if secondary_avail is None or secondary_installed_capacity_m3_min is None
            else secondary_installed_capacity_m3_min * secondary_avail,
            primary_pump_hours=None,
            secondary_pump_hours=None,
            primary_window_pressure=None,
            secondary_window_pressure=None,
            status="WAIT_ASSIST_OR_ROUTED_VOLUME",
        )

    to_primary = assist_zone_volume_m3 * assist
    to_secondary = assist_zone_volume_m3 * (1.0 - assist)
    primary_total = primary_zone_volume_m3 + to_primary

    primary_cap = (
        None
        if primary_avail is None or primary_installed_capacity_m3_min is None
        else primary_installed_capacity_m3_min * primary_avail
    )
    secondary_cap = (
        None
        if secondary_avail is None or secondary_installed_capacity_m3_min is None
        else secondary_installed_capacity_m3_min * secondary_avail
    )

    primary_hours = (
        None if primary_cap is None or primary_cap <= 0 else primary_total / (primary_cap * 60.0)
    )
    secondary_hours = (
        None if secondary_cap is None or secondary_cap <= 0 else to_secondary / (secondary_cap * 60.0)
    )

    primary_pressure = (
        None
        if response_window_h is None or response_window_h == 0 or primary_hours is None
        else primary_hours / response_window_h
    )
    secondary_pressure = (
        None
        if response_window_h is None or response_window_h == 0 or secondary_hours is None
        else secondary_hours / response_window_h
    )

    status = "ALLOCATED_WAIT_CAPACITY" if primary_hours is None or secondary_hours is None else "ALLOCATED"

    return DispatchResult(
        primary_zone_volume_m3=primary_zone_volume_m3,
        assist_zone_volume_to_primary_m3=to_primary,
        assist_zone_volume_to_secondary_m3=to_secondary,
        primary_total_volume_m3=primary_total,
        primary_available_capacity_m3_min=primary_cap,
        secondary_available_capacity_m3_min=secondary_cap,
        primary_pump_hours=primary_hours,
        secondary_pump_hours=secondary_hours,
        primary_window_pressure=primary_pressure,
        secondary_window_pressure=secondary_pressure,
        status=status,
    )
