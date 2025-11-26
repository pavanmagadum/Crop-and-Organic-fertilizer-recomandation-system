import joblib, pandas as pd, json, os, sys
from pathlib import Path
# ensure project root is on sys.path so `src` and `community` import correctly
proj_root = Path(__file__).resolve().parents[1]
if str(proj_root) not in sys.path:
    sys.path.insert(0, str(proj_root))
from src.conversion import predict_fertilizer_simple, convert_non_to_org
from community import db as cdb

# prepare input
input_data = {'region':'North','soil':'Loamy','N':300.0,'P':50.0,'K':150.0,'pH':6.5,'temperature':25.0,'humidity':70.0,'rainfall':800.0}

# load crop model
crop_pred = None
nf = None
try:
    crop_bundle = joblib.load('crop_model.joblib')
    artifacts = joblib.load('artifacts.joblib')
    enc = artifacts['encoders']; scaler = artifacts['scaler']; crop_model = crop_bundle['model']
    df = pd.DataFrame([{'region':input_data['region'],'soil_type':input_data['soil'],'N':input_data['N'],'P':input_data['P'],'K':input_data['K'],'pH':input_data['pH'],'temperature':input_data['temperature'],'humidity':input_data['humidity'],'rainfall':input_data['rainfall']}])
    for c,le in enc.items():
        df[c] = le.transform(df[c].astype(str))
    X = df[['region','soil_type','N','P','K','pH','temperature','humidity','rainfall']].values
    Xs = scaler.transform(X)
    crop_pred = crop_model.predict(Xs)[0]
except Exception as e:
    print('Crop model load/predict failed:', e)

# fertilizer prediction
try:
    fert_bundle = joblib.load('fert_model.joblib')
    fert_model = fert_bundle['model']; fert_le = fert_bundle['le']; cols = fert_bundle['columns']
    row = df.copy(); row = pd.get_dummies(row, columns=['region','soil_type'], drop_first=True)
    for c in cols:
        if c not in row.columns: row[c]=0
    Xf = row[cols].values; nf = fert_le.inverse_transform([fert_model.predict(Xf)[0]])[0]
except Exception:
    nf = predict_fertilizer_simple(input_data['N'], input_data['P'], input_data['K'], input_data['pH'], crop_pred)

conv = convert_non_to_org(nf)

# save to history for farmer1
try:
    cdb.save_history('farmer1', json.dumps(input_data), json.dumps({'crop': crop_pred, 'nf': nf, 'conv': conv}))
    print('Saved history for farmer1')
except Exception as e:
    print('Failed saving history:', e)

# create a small attachment and post a question
os.makedirs('community/uploads', exist_ok=True)
attach_path = os.path.join('community','uploads','demo_attachment.txt')
with open(attach_path,'w') as f:
    f.write('demo attachment content')
try:
    cdb.create_question('Demo question from farmer1', 'Please advise on fertilizer preparation steps.', 'farmer1', attachment_path=attach_path)
    print('Created question with attachment')
except Exception as e:
    print('Failed creating question:', e)

# print out stored rows
print('\n--- History rows for farmer1 ---')
for r in cdb.get_history('farmer1'):
    print(r)

print('\n--- Questions ---')
for q in cdb.list_questions():
    print(q)

print('\n--- Answers per question ---')
for q in cdb.list_questions():
    print('Question', q[0], 'answers:', cdb.get_answers(q[0]))
