from pathlib import Path
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder


def fert_nutrient_profile(name):
    n = name.lower()
    # return plausible ranges (low, high) for N, P, K
    if 'urea' in n or 'uan' in n:
        return (200, 500), (0, 120), (0, 150)
    if 'dap' in n or 'single super' in n or 'ssp' in n:
        return (0, 150), (150, 400), (0, 200)
    if 'mop' in n or 'potash' in n or 'potassium' in n:
        return (0, 200), (0, 150), (150, 450)
    if 'npk' in n or 'balanced' in n or '17-17-17' in n:
        return (100, 300), (100, 300), (100, 300)
    if 'ammonium' in n:
        return (150, 400), (0, 120), (0, 150)
    if 'calcium' in n and 'nitrate' in n:
        return (50, 200), (0, 150), (0, 150)
    if 'magnesium' in n and 'nitrate' in n:
        return (50, 200), (0, 150), (0, 150)
    if 'zinc' in n:
        return (0, 150), (0, 150), (0, 150)
    if 'gypsum' in n or 'calcium sulphate' in n:
        return (0, 150), (0, 150), (0, 150)
    # fallback generic
    return (50, 300), (20, 200), (20, 300)


def sample_for_fertilizer(name, n_samples=300, regions=None, soils=None, random_state=42):
    rng = np.random.RandomState(random_state)
    (n_lo, n_hi), (p_lo, p_hi), (k_lo, k_hi) = fert_nutrient_profile(name)
    Ns = rng.uniform(n_lo, n_hi, size=n_samples)
    Ps = rng.uniform(p_lo, p_hi, size=n_samples)
    Ks = rng.uniform(k_lo, k_hi, size=n_samples)
    phs = rng.uniform(5.0, 8.5, size=n_samples)
    temps = rng.uniform(12, 32, size=n_samples)
    hums = rng.uniform(20, 90, size=n_samples)
    rains = rng.uniform(50, 1200, size=n_samples)
    regions = regions or ['North', 'South', 'East', 'West', 'Central']
    soils = soils or ['Loamy', 'Sandy', 'Clayey', 'Silty']
    regs = rng.choice(regions, size=n_samples)
    sols = rng.choice(soils, size=n_samples)
    rows = []
    for i in range(n_samples):
        rows.append({'region': regs[i], 'soil_type': sols[i], 'N': Ns[i], 'P': Ps[i], 'K': Ks[i], 'pH': phs[i], 'temperature': temps[i], 'humidity': hums[i], 'rainfall': rains[i], 'label': name})
    return pd.DataFrame(rows)


def main():
    proj = Path(__file__).resolve().parent
    fm = pd.read_csv(proj / 'data' / 'fertilizer_mapping.csv')
    ferts = list(fm['nonorganic'].astype(str).unique())
    # small check
    print('Found fertilizers:', ferts)
    # load some real regions/soils from crop_data to sample from
    try:
        crop_df = pd.read_csv(proj / 'data' / 'crop_data.csv')
        regions = sorted(crop_df['region'].unique().tolist())
        soils = sorted(crop_df['soil_type'].unique().tolist())
    except Exception:
        regions = ['North','South','East','West','Central']
        soils = ['Loamy','Sandy','Clayey','Silty']

    parts = []
    per_class = max(200, int(300))
    for f in ferts:
        df_s = sample_for_fertilizer(f, n_samples=per_class, regions=regions, soils=soils, random_state=hash(f) % 9999)
        parts.append(df_s)

    data = pd.concat(parts, ignore_index=True)
    # shuffle
    data = data.sample(frac=1.0, random_state=42).reset_index(drop=True)

    # Prepare X and y
    X = data[['region','soil_type','N','P','K','pH','temperature','humidity','rainfall']].copy()
    X = pd.get_dummies(X, columns=['region','soil_type'], drop_first=True)
    cols = list(X.columns)
    y = data['label']

    le = LabelEncoder()
    y_enc = le.fit_transform(y)

    print('Training dataset size:', X.shape)
    clf = RandomForestClassifier(n_estimators=200, random_state=42)
    clf.fit(X.values, y_enc)

    # Save model bundle
    out = {'model': clf, 'le': le, 'columns': cols}
    joblib.dump(out, proj / 'fert_model.joblib')
    (proj / 'models').mkdir(exist_ok=True)
    joblib.dump(out, proj / 'models' / 'fert_model.joblib')
    print('Saved new fert_model.joblib with classes:', le.classes_)


if __name__ == '__main__':
    main()
