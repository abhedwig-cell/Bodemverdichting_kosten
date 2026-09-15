"""Pump-energy identity with explicit operating-point inputs."""

from __future__ import annotations


def pump_energy_kwh(
    pumped_volume_m3: float | None,
    total_dynamic_head_m: float | None,
    pump_efficiency: float | None,
    *,
    water_density_kg_m3: float = 1000.0,
    gravity_m_s2: float = 9.80665,
) -> float | None:
    """Return hydraulic pumping energy in kWh.

    E = rho * g * H * V / (eta * 3.6e6)

    No head or efficiency defaults are provided because those are asset/operating-state
    evidence, not universal project constants.
    """
    if pumped_volume_m3 is None or total_dynamic_head_m is None or pump_efficiency is None:
        return None

    if pumped_volume_m3 < 0:
        raise ValueError("pumped_volume_m3 must be >= 0")
    if total_dynamic_head_m < 0:
        raise ValueError("total_dynamic_head_m must be >= 0")
    if not 0 < pump_efficiency <= 1:
        raise ValueError("pump_efficiency must be in (0, 1]")
    if water_density_kg_m3 <= 0 or gravity_m_s2 <= 0:
        raise ValueError("physical constants must be > 0")

    return (
        water_density_kg_m3
        * gravity_m_s2
        * total_dynamic_head_m
        * pumped_volume_m3
        / (pump_efficiency * 3.6e6)
    )
