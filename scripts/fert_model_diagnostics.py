import sys
from pathlib import Path
proj_root = Path(__file__).resolve().parents[1]
if str(proj_root) not in sys.path:
    sys.path.insert(0, str(proj_root))

import joblib
import pandas as pd
from src.conversion import predict_fertilizer_simple

print('Project root:', proj_root)

artifacts = None
fert_bundle = None
try:
    artifacts = joblib.load('artifacts.joblib')
    print('Loaded artifacts.joblib')
except Exception as e:
    print('Could not load artifacts.joblib:', e)

try:
    fert_bundle = joblib.load('fert_model.joblib')
    print('Loaded fert_model.joblib')
except Exception as e:
    print('Could not load fert_model.joblib:', e)

if not fert_bundle:
    print('No fert model; aborting diagnostics.')
    sys.exit(0)

fert_model = fert_bundle.get('model')
fert_le = fert_bundle.get('le')
cols = fert_bundle.get('columns')
print('Model type:', type(fert_model))
if fert_le is not None:
    try:
        classes = list(fert_le.classes_)
        print('Label classes (fertilizers):', classes)
    except Exception as e:
        print('Could not read label encoder classes:', e)

print('Expected feature columns for fertilizer model:', cols)

enc = artifacts.get('encoders') if artifacts else {}
scaler = artifacts.get('scaler') if artifacts else None

# helper to prepare row and predict
import numpy as np

def predict_for_input(tc):
    df = pd.DataFrame([tc])
    # apply encoders if present
    try:
        for c,le in (enc.items() if enc else []):
            if c in df.columns:
                df[c] = le.transform(df[c].astype(str))
    except Exception as e:
        print('  encoder transform failed:', e)
    row = df.copy()
    row = pd.get_dummies(row, columns=['region','soil_type'], drop_first=True)
    for c in cols:
        if c not in row.columns:
            row[c] = 0
    Xf = row[cols].values
    try:
        pred_idx = fert_model.predict(Xf)[0]
        pred_label = fert_le.inverse_transform([pred_idx])[0] if fert_le is not None else str(pred_idx)
    except Exception as e:
        pred_label = f'prediction error: {e}'
    return pred_label

base = {'region':'North','soil_type':'Loamy','pH':6.5,'temperature':25,'humidity':70,'rainfall':800}

print('\nSensitivity: vary Nitrogen (N) with fixed P=50,K=50')
ns = list(range(0,401,50))
preds = []
for n in ns:
    tc = base.copy(); tc.update({'N':n,'P':50,'K':50})
    p = predict_for_input(tc)
    preds.append((n,p))
    print(' N=',n,'->',p)
print('Unique predictions for N variation:', set([p for n,p in preds]))

print('\nSensitivity: vary Phosphorus (P) with fixed N=100,K=50')
ps = list(range(0,301,50))
preds_p = []
for v in ps:
    tc = base.copy(); tc.update({'N':100,'P':v,'K':50})
    p = predict_for_input(tc)
    preds_p.append((v,p))
    print(' P=',v,'->',p)
print('Unique predictions for P variation:', set([p for v,p in preds_p]))

print('\nSensitivity: vary Potassium (K) with fixed N=100,P=50')
ks = list(range(0,401,50))
preds_k = []
for v in ks:
    tc = base.copy(); tc.update({'N':100,'P':50,'K':v})
    p = predict_for_input(tc)
    preds_k.append((v,p))
    print(' K=',v,'->',p)
print('Unique predictions for K variation:', set([p for v,p in preds_k]))

print('\nSensitivity: vary soil types with N=100,P=50,K=50')
soils = ['Loamy','Sandy','Clayey','Silty']
for s in soils:
    tc = base.copy(); tc.update({'N':100,'P':50,'K':50,'soil_type':s})
    p = predict_for_input(tc)
    print(' soil=',s,'->',p)

print('\nTest complete')
