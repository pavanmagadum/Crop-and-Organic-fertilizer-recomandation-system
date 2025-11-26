from pathlib import Path
import joblib
from pprint import pprint

p = Path('models') / 'fert_model.joblib'
if not p.exists():
    p = Path('fert_model.joblib')
print('Loading from', p)
try:
    obj = joblib.load(p)
    print('Loaded type:', type(obj))
    if isinstance(obj, dict):
        print('Keys:')
        pprint(list(obj.keys()))
        if 'columns' in obj:
            print('Columns sample (first 30):')
            print(obj['columns'][:30])
        if 'le' in obj:
            print('Label encoder type:', type(obj['le']))
    else:
        print('Object repr:')
        pprint(obj)
except Exception as e:
    print('Error loading joblib:', e)
