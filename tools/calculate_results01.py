"""Reproduce doc 112 RESULTS01 scenarios; no admitted damage coefficients.

Run from repository root: python tools/calculate_results01.py
Inputs and source boundaries are documented in doc 112 sections I/J.
Uses existing physical identities, never populates national calculation surfaces.
"""
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.transfer.volume import generated_increment_m3
from src.water_system.energy import pump_energy_kwh


def calculate():
    maize = []
    for load, fraction in [(5, .04), (10, .15)]:
        lost_ds = 16531 * fraction
        gross = lost_ds * 998 / 1000 * .130
        maize.append(dict(axle_load_Mg=load, assumed_loss_fraction=fraction,
                          lost_harvest_kg_ds_ha=lost_ds,
                          harvest_energy_book_eur_ha=gross,
                          after_4pct_conservation_eur_ha=gross * .96,
                          private_marginal_damage_eur_ha=None))
    # CBS national component production / ALL grass area: not specialist yields.
    grass = {name: mass * 1e6 / 950000 for name, mass in
             [('silage', 5918), ('hay', 247), ('grazed_residual', 1812)]}
    grass_book = grass['silage'] * 916 / 1000 * .112
    grass_sensitivity = [dict(improvement_fraction=b,
                             assumed_current_silage_kg_ds_ha=grass['silage'],
                             benefit_energy_book_eur_ha=grass_book * b,
                             loss_fraction_of_improved_reference=b / (1 + b))
                         for b in [.03, .05, .17, .23]]
    pumps = []
    for name, intensity, volume_million in [
            ('Leemans_1', 39, 70.5), ('Leemans_3', 32, 113.8),
            ('Lely_2', 48, 24.7), ('Lely_3', 41, 11.3), ('Lely_4', 39, 3.7)]:
        e = 1 / intensity
        # Only H/eta is identifiable from annual kWh/m3, not H and eta separately.
        h_over_eta = e / pump_energy_kwh(1, 1, 1)
        assert abs(pump_energy_kwh(1, h_over_eta, 1) - e) < 1e-12
        pumps.append(dict(asset=name, reported_m3_kwh=intensity,
                          reported_volume_million_m3=volume_million,
                          derived_kwh_m3=e, equivalent_head_over_eta_m=h_over_eta,
                          scenario_eur_m3_at_025_eur_kwh=e * .25,
                          conditional_energy_eur_100m3=100 * e * .25,
                          conditional_energy_eur_120m3=120 * e * .25))
    assert generated_increment_m3(1, 10) == 100
    assert generated_increment_m3(1, 12) == 120
    assert generated_increment_m3(None, 10) is None
    return dict(status='ILLUSTRATIVE_ACCOUNTING_ONLY_NOT_DAMAGE_ADMISSION',
                maize=maize, grass_component_kg_ds_per_all_grass_ha=grass,
                grass_silage_book_eur_per_all_grass_ha=grass_book,
                grass_sensitivity=grass_sensitivity, pumps=pumps,
                marginal_pump_cost_eur_m3=None, national_damage_eur=None)


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2, allow_nan=False))
