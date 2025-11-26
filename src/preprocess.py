import pandas as pd, joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler
def load_data(path):
    return pd.read_csv(path)
def preprocess(df, save_artifacts=False, art_path='models/artifacts.joblib'):
    d = df.copy().drop_duplicates().fillna(df.median(numeric_only=True))
    encoders = {}
    for c in ['region','soil_type']:
        le = LabelEncoder()
        d[c] = le.fit_transform(d[c].astype(str))
        encoders[c] = le
    X = d.drop(columns=['crop']); y = d['crop']
    scaler = StandardScaler()
    Xs = scaler.fit_transform(X)
    if save_artifacts:
        joblib.dump({'encoders':encoders,'scaler':scaler}, art_path)
    return Xs, y, encoders, scaler
if __name__=='__main__':
    df = load_data('../data/crop_data.csv')
    preprocess(df, save_artifacts=True)
