import sys
from pathlib import Path
proj_root = Path(__file__).resolve().parents[1]
if str(proj_root) not in sys.path:
    sys.path.insert(0, str(proj_root))

import joblib
import pandas as pd
from src.conversion import predict_fertilizer_simple

print('Project root:', proj_root)
# load artifacts if present
artifacts = None
try:
    artifacts = joblib.load('artifacts.joblib')
    print('Loaded artifacts.joblib')
except Exception as e:
    print('Could not load artifacts.joblib:', e)

fert_bundle = None
try:
    fert_bundle = joblib.load('fert_model.joblib')
    print('Loaded fert_model.joblib')
except Exception as e:
    print('Could not load fert_model.joblib:', e)

# Define test cases: vary N,P,K and soil types
test_cases = [
    {'region':'North','soil_type':'Loamy','N':300,'P':50,'K':150,'pH':6.5,'temperature':25,'humidity':70,'rainfall':800},
    {'region':'North','soil_type':'Sandy','N':50,'P':200,'K':150,'pH':6.5,'temperature':25,'humidity':70,'rainfall':800},
    {'region':'North','soil_type':'Clayey','N':50,'P':50,'K':300,'pH':6.5,'temperature':25,'humidity':70,'rainfall':800},
    {'region':'South','soil_type':'Loamy','N':100,'P':100,'K':100,'pH':6.5,'temperature':25,'humidity':70,'rainfall':800},
]

# Utility to run fert_model prediction if available
if fert_bundle:
    fert_model = fert_bundle.get('model')
    fert_le = fert_bundle.get('le')
    cols = fert_bundle.get('columns')
else:
    fert_model = fert_le = cols = None

# artifacts may contain encoders and scaler
enc = artifacts.get('encoders') if artifacts else {}
scaler = artifacts.get('scaler') if artifacts else None

print('\nRunning test cases:')
for i,tc in enumerate(test_cases, start=1):
    print('\nCase', i, tc)
    df = pd.DataFrame([tc])
    # try to encode categorical using encoders if available
    try:
        for c,le in (enc.items() if enc else []):
            df[c] = le.transform(df[c].astype(str))
    except Exception as e:
        print('  Warning: encoder transform failed:', e)
    # prepare fert features if fert_model exists
    if fert_model and cols:
        row = df.copy()
        row = pd.get_dummies(row, columns=['region','soil_type'], drop_first=True)
        for c in cols:
            if c not in row.columns:
                row[c] = 0
        Xf = row[cols].values
        try:
            pred_idx = fert_model.predict(Xf)[0]
            pred_label = fert_le.inverse_transform([pred_idx])[0] if fert_le is not None else str(pred_idx)
            print('  fert_model prediction:', pred_label)
        except Exception as e:
            print('  fert_model prediction failed:', e)
            print('  fallback heuristic:', predict_fertilizer_simple(tc['N'], tc['P'], tc['K'], tc.get('pH'), None))
    else:
        print('  fert_model not available; using fallback:')
        print('  fallback heuristic:', predict_fertilizer_simple(tc['N'], tc['P'], tc['K'], tc.get('pH'), None))

print('\nDone')
