from __future__ import annotations
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def rows(path):
    with path.open('r',encoding='utf-8',newline='') as f:return list(csv.DictReader(f))

def validate():
    errors=[]
    req={r['data_request_id']:r for r in rows(ROOT/'data_requests/data_request_register.csv')}.get('DR_SM_LAND_USE')
    if not req:return ['missing DR_SM_LAND_USE']
    if req.get('input_readiness_status')!='PARTIAL_EVIDENCE':errors.append('DR_SM_LAND_USE must be PARTIAL_EVIDENCE; 1998 crop is not admitted')
    required=('EV_TOL_LAND_USE_NEAR_PERIOD','EV_TOL_LGN3_PRE_EVENT','EV_TOL_LGN4_POST_EVENT','EV_LGN_CROP_ROTATION_CAUTION','EV_BRP_PUBLIC_ARCHIVE_START_2009')
    for eid in required:
        if eid not in req.get('current_evidence_ids',''):errors.append(f'DR_SM_LAND_USE missing {eid}')
    if 'CL_TOL_1998_LAND_USE_GATE' not in req.get('current_claim_ids',''):errors.append('land-use gate claim missing')
    boundary=(req.get('blocking_reason','')+' '+req.get('request_notes','')).lower()
    for phrase in ('1995','1999/2000','2009','crop rotation','representative','bare soil','missing'):
        if phrase not in boundary:errors.append(f'land-use guardrail missing {phrase!r}')
    evidence={r['evidence_id']:r for r in rows(ROOT/'evidence/evidence_register.csv')}
    if evidence.get('EV_TOL_LGN3_PRE_EVENT',{}).get('evidence_value')!='25':errors.append('LGN3 resolution/context changed')
    if evidence.get('EV_BRP_PUBLIC_ARCHIVE_START_2009',{}).get('evidence_value')!='2009':errors.append('BRP public historical lower bound changed')
    caution=evidence.get('EV_LGN_CROP_ROTATION_CAUTION',{})
    if caution.get('evidence_status')!='QUALIFIED' or 'crop rotation' not in caution.get('evidence_statement','').lower():errors.append('crop-rotation guardrail not qualified')
    claims={r['claim_id']:r for r in rows(ROOT/'evidence/claims.csv')}
    claim=claims.get('CL_TOL_1998_LAND_USE_GATE',{})
    if claim.get('qualification_status')!='QUALIFIED':errors.append('land-use gate claim not QUALIFIED')
    if 'representative arable crop' not in claim.get('guardrail',''):errors.append('representative-crop exclusion weakened')
    trace={r['capability_id']:r for r in rows(ROOT/'model/traceability.csv')}.get('CAP_ATTRIB',{})
    if trace.get('capability_status')!='DATA_GATED':errors.append('CAP_ATTRIB must remain DATA_GATED')
    if 'CL_TOL_1998_LAND_USE_GATE' not in trace.get('evidence_or_claim_ids',''):errors.append('CAP_ATTRIB trace missing land-use gate')
    forbidden=(ROOT/'data/land_use/tollebeek_1998_crop.csv',ROOT/'data/land_use/tollebeek_1998_land_use.csv')
    for p in forbidden:
        if p.exists():errors.append(f'unexpected admitted 1998 land-use dataset: {p.relative_to(ROOT)}')
    return errors

def main():
    errors=validate()
    if errors:
        print('Tollebeek land-use gate validation FAILED')
        for e in errors:print(f'ERROR: {e}')
        return 1
    print('Tollebeek land-use gate validation passed.')
    print('Validated historical context routes, crop-rotation temporal guardrail, BRP archive bound and no-admit 1998 crop semantics.')
    return 0
if __name__=='__main__':raise SystemExit(main())
