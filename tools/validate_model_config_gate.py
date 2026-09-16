from __future__ import annotations
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PROD='50346642bd565f79134ea17d5462e544b354998c'
STATUS='992a5c657bfe10a10100f92e0cb77c4825ae65b6'
GOV='80c6faaa8a277d9596a6da7bc5d2244c0df1bb82'

def rows(path):
    with path.open('r',encoding='utf-8',newline='') as f:return list(csv.DictReader(f))

def validate():
    errors=[]
    req={r['data_request_id']:r for r in rows(ROOT/'data_requests/data_request_register.csv')}.get('DR_SM_MODEL_CONFIG')
    if not req:return ['missing DR_SM_MODEL_CONFIG']
    if req.get('input_readiness_status')!='PARTIAL_EVIDENCE':errors.append('DR_SM_MODEL_CONFIG must remain PARTIAL_EVIDENCE; no concrete configuration is admitted')
    for eid in ('EV_SWAP5_SCIENTIFIC_PRODUCTION_BASELINE','EV_SWAP5_STATUS_A_ACCEPTANCE_AUTHORITY','EV_SWAP5_LIVE_GOVERNANCE_HEAD'):
        if eid not in req.get('current_evidence_ids',''):errors.append(f'DR_SM_MODEL_CONFIG missing {eid}')
    if 'CL_TOL_MODEL_CONFIG_GATE' not in req.get('current_claim_ids',''):errors.append('model-config gate claim missing')
    evidence={r['evidence_id']:r for r in rows(ROOT/'evidence/evidence_register.csv')}
    if evidence.get('EV_SWAP5_SCIENTIFIC_PRODUCTION_BASELINE',{}).get('evidence_value')!=PROD:errors.append('SWAP5 production pin changed')
    if evidence.get('EV_SWAP5_STATUS_A_ACCEPTANCE_AUTHORITY',{}).get('evidence_value')!=STATUS:errors.append('SWAP5 Status-A authority changed')
    if evidence.get('EV_SWAP5_LIVE_GOVERNANCE_HEAD',{}).get('evidence_value')!=GOV:errors.append('reviewed live governance head changed')
    claim={r['claim_id']:r for r in rows(ROOT/'evidence/claims.csv')}.get('CL_TOL_MODEL_CONFIG_GATE',{})
    if claim.get('qualification_status')!='QUALIFIED':errors.append('model-config gate claim not QUALIFIED')
    guard=(claim.get('guardrail','')+' '+req.get('blocking_reason','')+' '+req.get('request_notes','')).lower()
    for phrase in ('drainage','initial','managed-boundary','crop','current/reference','default','no source-model run'):
        if phrase not in guard:errors.append(f'model-config guardrail missing {phrase!r}')
    trace={r['capability_id']:r for r in rows(ROOT/'model/traceability.csv')}.get('CAP_ATTRIB',{})
    if trace.get('capability_status')!='DATA_GATED':errors.append('CAP_ATTRIB must remain DATA_GATED')
    if 'Current depth-resolved Tollebeek current/reference states are not admitted' not in trace.get('broken_link',''):errors.append('canonical current/reference guardrail weakened')
    forbidden=(ROOT/'data/model/tollebeek_model_configurations.csv',ROOT/'model/tollebeek_model_configurations.csv',ROOT/'data/configuration/tollebeek_model_configuration.csv')
    for p in forbidden:
        if p.exists():errors.append(f'unexpected admitted model configuration dataset: {p.relative_to(ROOT)}')
    return errors

def main():
    errors=validate()
    if errors:
        print('Tollebeek model-config gate validation FAILED')
        for e in errors: print(f'ERROR: {e}')
        return 1
    print('Tollebeek model-config gate validation passed.')
    print('Validated pinned SWAP5 authority chain and explicit no-admit configuration semantics.')
    return 0
if __name__=='__main__':raise SystemExit(main())
