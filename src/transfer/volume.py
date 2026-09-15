"""Physical source-volume identities for the project.

These functions contain no Tollebeek-specific defaults and preserve null semantics.
"""

from __future__ import annotations


def generated_increment_m3(
    affected_area_ha: float | None,
    delta_runoff_mm: float | None,
) -> float | None:
    """Convert a qualified runoff-depth difference to generated parcel volume.

    V = 10 * area_ha * delta_runoff_mm

    Returns None when an input is unknown. Unknown must not become zero.
    Negative delta_runoff_mm is permitted because a matched current/reference
    comparison can in principle yield a decrease.
    """
    if affected_area_ha is None or delta_runoff_mm is None:
        return None
    if affected_area_ha < 0:
        raise ValueError("affected_area_ha must be >= 0")
    return 10.0 * affected_area_ha * delta_runoff_mm
