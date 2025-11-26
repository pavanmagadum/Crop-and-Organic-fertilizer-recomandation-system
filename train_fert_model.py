from pathlib import Path
import sys
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score


def synth_label(row):
    # Simple heuristic to pick a nonorganic fertilizer label
    N = float(row['N']); P = float(row['P']); K = float(row['K'])
    crop = str(row.get('crop','')).lower()
    # crop-based overrides
    if crop in ('rice','sugarcane'):
        return 'Urea'
    if crop in ('groundnut','maize') and K > N:
        return 'MOP (Potash)'
    # balanced check
    vals = [N,P,K]
    mx = max(vals); mn = min(vals)
    if mx - mn < 0.1 * mx:
        return 'NPK 20-20-20'
    # dominant nutrient
    if N >= P and N >= K:
        return 'Urea'
    if P >= N and P >= K:
        return 'DAP'
    return 'MOP (Potash)'


def main():
    proj = Path(__file__).resolve().parent
    data_path = proj / 'data' / 'fertilizer_mapping.csv'
    # Use crop_data to synthesize features
    df = pd.read_csv(proj / 'data' / 'crop_data.csv')
    # create synthetic target using heuristics
    df['nonorganic'] = df.apply(synth_label, axis=1)

    # features: region, soil_type, N,P,K,pH,temperature,humidity,rainfall
    X = df[['region','soil_type','N','P','K','pH','temperature','humidity','rainfall']].copy()
    X = pd.get_dummies(X, columns=['region','soil_type'], drop_first=True)
    cols = list(X.columns)
    y = df['nonorganic']

    le = LabelEncoder(); y_enc = le.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X.values, y_enc, test_size=0.2, random_state=42, stratify=y_enc)

    clf = RandomForestClassifier(n_estimators=150, random_state=42)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print('Fertilizer model accuracy (synthetic labels):', acc)
    print(classification_report(y_test, y_pred, target_names=le.classes_))

    out = {'model': clf, 'le': le, 'columns': cols}
    models_dir = proj / 'models'
    models_dir.mkdir(exist_ok=True)
    joblib.dump(out, proj / 'fert_model.joblib')
    joblib.dump(out, models_dir / 'fert_model.joblib')
    print('Saved fert_model.joblib to root and models/')


if __name__ == '__main__':
    main()
