from __future__ import annotations

import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def rows(path):
    with path.open('r',encoding='utf-8',newline='') as f: return list(csv.DictReader(f))

def validate():
    errors=[]
    req={r['data_request_id']:r for r in rows(ROOT/'data_requests/data_request_register.csv')}.get('DR_SM_INITIAL_STATE')
    if not req: return ['missing DR_SM_INITIAL_STATE']
    if req.get('input_readiness_status')!='PARTIAL_EVIDENCE': errors.append('DR_SM_INITIAL_STATE must remain PARTIAL_EVIDENCE; no initial state is admitted')
    for eid in ('EV_TOL_INITIAL_DEEP_GLD','EV_TOL_INITIAL_SHALLOW_SEARCH','EV_TOL_INITIAL_SHALLOW_NEARBY_CONTEXT'):
        if eid not in req.get('current_evidence_ids',''): errors.append(f'DR_SM_INITIAL_STATE missing {eid}')
    if 'CL_TOL_INITIAL_STATE_GATE' not in req.get('current_claim_ids',''): errors.append('DR_SM_INITIAL_STATE missing gate claim')
    boundary=(req.get('blocking_reason','')+' '+req.get('request_notes','')).lower()
    for phrase in ('deep','piezometric','target peil','fully saturated','missing'):
        if phrase not in boundary: errors.append(f'initial-state boundary must preserve {phrase!r} guardrail')
    evidence={r['evidence_id']:r for r in rows(ROOT/'evidence/evidence_register.csv')}
    deep=evidence.get('EV_TOL_INITIAL_DEEP_GLD',{})
    if deep.get('evidence_status')!='QUALIFIED' or 'not an observed phreatic' not in deep.get('guardrail',''):
        errors.append('deep GLD evidence must remain qualified-with-phreatic-exclusion evidence')
    shallow=evidence.get('EV_TOL_INITIAL_SHALLOW_SEARCH',{})
    if shallow.get('evidence_value')!='0' or shallow.get('evidence_unit')!='inside-OT.02 shallow candidate series': errors.append('shallow-search negative result changed')
    claims={r['claim_id']:r for r in rows(ROOT/'evidence/claims.csv')}
    claim=claims.get('CL_TOL_INITIAL_STATE_GATE',{})
    if claim.get('qualification_status')!='QUALIFIED': errors.append('initial-state gate claim not QUALIFIED')
    quals={r['qualification_id']:r for r in rows(ROOT/'evidence/qualification_register.csv')}
    for qid in ('Q_TOL_INITIAL_DEEP_GLD','Q_TOL_INITIAL_SHALLOW_SEARCH','Q_TOL_INITIAL_SHALLOW_NEARBY_CONTEXT'):
        if qid not in quals: errors.append(f'missing qualification {qid}')
    trace={r['capability_id']:r for r in rows(ROOT/'model/traceability.csv')}.get('CAP_ATTRIB',{})
    if trace.get('capability_status')!='DATA_GATED': errors.append('CAP_ATTRIB must remain DATA_GATED')
    # No canonical initial-state dataset/protocol is allowed in this route-only workunit.
    forbidden=[ROOT/'data/hydrology/tollebeek_initial_state.csv',ROOT/'data/hydrology/tollebeek_1998_initial_state.csv']
    for p in forbidden:
        if p.exists(): errors.append(f'unexpected canonical initial-state dataset: {p.relative_to(ROOT)}')
    return errors

def main():
    errors=validate()
    if errors:
        print('Tollebeek initial-state gate validation FAILED')
        for e in errors: print(f'ERROR: {e}')
        return 1
    print('Tollebeek initial-state gate validation passed.')
    print('Validated route evidence, deep-vs-phreatic boundary, negative shallow screening and no-admit state semantics.')
    return 0

if __name__=='__main__': raise SystemExit(main())
