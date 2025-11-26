from pathlib import Path
import sys, os
proj_root = Path(__file__).resolve().parent
if str(proj_root) not in sys.path:
    sys.path.insert(0, str(proj_root))

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

from src import preprocess as pre


def main():
    data_path = proj_root / 'data' / 'crop_data.csv'
    print('Loading data from', data_path)
    df = pd.read_csv(data_path)

    print('Preprocessing...')
    Xs, y, encoders, scaler = pre.preprocess(df, save_artifacts=False)

    X_train, X_test, y_train, y_test = train_test_split(Xs, y, test_size=0.2, random_state=42, stratify=y)

    print('Training RandomForestClassifier...')
    clf = RandomForestClassifier(n_estimators=200, random_state=42)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f'Accuracy on test set: {acc:.4f}')
    print('Classification report:')
    print(classification_report(y_test, y_pred))

    # Save model bundle expected by app
    out_crop = {'model': clf}
    out_artifacts = {'encoders': encoders, 'scaler': scaler}

    # ensure models dir exists
    models_dir = proj_root / 'models'
    models_dir.mkdir(exist_ok=True)

    crop_path = proj_root / 'crop_model.joblib'
    art_path = proj_root / 'artifacts.joblib'
    models_crop_path = models_dir / 'crop_model.joblib'
    models_art_path = models_dir / 'artifacts.joblib'

    print('Saving crop model to', crop_path)
    joblib.dump(out_crop, crop_path)
    joblib.dump(out_crop, models_crop_path)
    print('Saving artifacts to', art_path)
    joblib.dump(out_artifacts, art_path)
    joblib.dump(out_artifacts, models_art_path)

    print('Done. Files written:')
    print(' -', crop_path)
    print(' -', art_path)
    print(' -', models_crop_path)
    print(' -', models_art_path)


if __name__ == '__main__':
    main()
