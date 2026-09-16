from __future__ import annotations

import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def rows(path):
    with path.open('r',encoding='utf-8',newline='') as f: return list(csv.DictReader(f))

def validate():
    errors=[]
    req={r['data_request_id']:r for r in rows(ROOT/'data_requests/data_request_register.csv')}.get('DR_SM_MANAGED_BOUNDARY')
    if not req: return ['missing DR_SM_MANAGED_BOUNDARY']
    if req.get('input_readiness_status')!='PARTIAL_EVIDENCE': errors.append('DR_SM_MANAGED_BOUNDARY must remain PARTIAL_EVIDENCE; no event boundary is admitted')
    required=('EV_TOL_BOUNDARY_HISTORICAL_SYSTEM','EV_TOL_BOUNDARY_POST1998_REDESIGN','EV_TOL_BOUNDARY_1998_CRISIS','EV_TOL_BOUNDARY_OWNER_ARCHIVE_ROUTE')
    for eid in required:
        if eid not in req.get('current_evidence_ids',''): errors.append(f'DR_SM_MANAGED_BOUNDARY missing {eid}')
    if 'CL_TOL_1998_MANAGED_BOUNDARY_GATE' not in req.get('current_claim_ids',''): errors.append('managed-boundary gate claim missing')
    boundary=(req.get('blocking_reason','')+' '+req.get('request_notes','')).lower()
    for phrase in ('1998','ijsvogel','streefpeil','urkervaart','missing'):
        if phrase not in boundary: errors.append(f'managed-boundary guardrail missing {phrase!r}')
    evidence={r['evidence_id']:r for r in rows(ROOT/'evidence/evidence_register.csv')}
    hist=evidence.get('EV_TOL_BOUNDARY_HISTORICAL_SYSTEM',{})
    statement=hist.get('evidence_statement','')
    for phrase in ('De Rietgors','De Fuut','De Kievit','2.600','0.670','1.000','Urkervaart'):
        if phrase not in statement: errors.append(f'historical-system evidence missing {phrase!r}')
    if hist.get('evidence_status')!='QUALIFIED': errors.append('historical-system evidence must be QUALIFIED')
    post=evidence.get('EV_TOL_BOUNDARY_POST1998_REDESIGN',{})
    if 'not 1998 boundary inputs' not in post.get('guardrail',''): errors.append('post-1998 redesign exclusion weakened')
    route=evidence.get('EV_TOL_BOUNDARY_OWNER_ARCHIVE_ROUTE',{})
    if route.get('evidence_status')!='QUALIFIED': errors.append('owner archive acquisition route not QUALIFIED')
    claims={r['claim_id']:r for r in rows(ROOT/'evidence/claims.csv')}
    claim=claims.get('CL_TOL_1998_MANAGED_BOUNDARY_GATE',{})
    if claim.get('qualification_status')!='QUALIFIED': errors.append('managed-boundary gate claim not QUALIFIED')
    if 'current IJsvogel' not in claim.get('guardrail',''): errors.append('claim must exclude current IJsvogel as 1998 substitute')
    trace={r['capability_id']:r for r in rows(ROOT/'model/traceability.csv')}.get('CAP_MANAGED_BOUNDARY',{})
    if trace.get('capability_status')!='PARTIAL_METHOD_READY': errors.append('CAP_MANAGED_BOUNDARY status changed unexpectedly')
    if 'CL_TOL_1998_MANAGED_BOUNDARY_GATE' not in trace.get('evidence_or_claim_ids',''): errors.append('CAP_MANAGED_BOUNDARY traceability missing gate claim')
    forbidden=(
        ROOT/'data/hydrology/tollebeek_1998_managed_boundary.csv',
        ROOT/'data/hydrology/tollebeek_managed_boundary.csv',
        ROOT/'data/water_system/tollebeek_1998_managed_boundary.csv',
    )
    for p in forbidden:
        if p.exists(): errors.append(f'unexpected admitted managed-boundary dataset: {p.relative_to(ROOT)}')
    return errors

def main():
    errors=validate()
    if errors:
        print('Tollebeek managed-boundary gate validation FAILED')
        for e in errors: print(f'ERROR: {e}')
        return 1
    print('Tollebeek managed-boundary gate validation passed.')
    print('Validated historical-system distinction, post-1998 exclusion, owner acquisition route and no-admit boundary semantics.')
    return 0

if __name__=='__main__': raise SystemExit(main())
