"""Synthetic off-site storage experiment, doc112 Q; not empirical damage evidence.
Run: python tools/calculate_offsite_storage_sensitivity.py
All inflows are assumed at the receiving store, never parcel runoff.
"""
import json
import math

def simulate(inflow, capacity, storage_limit):
    # One-hour intervals; inflow and pumping uniform within each interval.
    stored = pumped = overflow = peak = 0.0
    for incoming in inflow:
        out = min(capacity, stored + incoming)
        stored += incoming - out
        spilled = max(0.0, stored - storage_limit)
        stored -= spilled
        pumped += out
        overflow += spilled
        peak = max(peak, stored)
    assert math.isclose(sum(inflow), stored + pumped + overflow, abs_tol=1e-9)
    return dict(inflow_m3=sum(inflow), pumped_m3=pumped,
                overflow_m3=overflow, end_storage_m3=stored,
                peak_stored_m3=peak)

def calculate():
    # Two zero-inflow hours allow all retained water to drain.
    ref = [80,80,80,80,0,0]
    fast = [240,80,0,0,0,0]
    extra = [240,160,0,0,0,0]
    cases = {n: simulate(q,100,150) for n,q in
             [('reference',ref),('same_volume_faster',fast),('extra_volume',extra)]}
    cases['extra_volume_more_storage'] = simulate(extra,100,200)
    cases['extra_volume_more_capacity'] = simulate(extra,125,150)
    cases['fast_more_storage'] = simulate(fast,100,200)
    assert cases['reference']['pumped_m3'] == cases['same_volume_faster']['pumped_m3'] == 320
    assert cases['same_volume_faster']['peak_stored_m3'] == 140
    assert cases['extra_volume']['overflow_m3'] == 50
    assert cases['extra_volume_more_storage']['overflow_m3'] == 0
    assert cases['extra_volume_more_capacity']['overflow_m3'] == 0
    assert cases['fast_more_storage'] == cases['same_volume_faster']
    return dict(status='SYNTHETIC_SYSTEM_SENSITIVITY_ONLY',dt_hours=1,
                initial_storage_m3=0,assumed_outflow_capacity_m3_h=100,
                assumed_storage_limit_m3=150,cases=cases,
                monetary_damage_eur=None)
if __name__ == '__main__':
    print(json.dumps(calculate(),indent=2,allow_nan=False))
