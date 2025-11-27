import pandas as pd
from pathlib import Path
proj = Path(__file__).resolve().parents[1]
df = pd.read_csv(proj / 'data' / 'crop_data.csv')
fm = pd.read_csv(proj / 'data' / 'fertilizer_mapping.csv')
fert_list = list(fm['nonorganic'].astype(str))

# helper: select candidate rows
results = {}

# Define search rules for each fertilizer name (heuristic)
rules = {
    'Urea': lambda r: r['N'] >= 350,
    'Urea Ammonium Nitrate (UAN)': lambda r: r['N'] >= 340 and r['K'] < r['N'],
    'Urea Ammonium Nitrate': lambda r: r['N'] >= 340 and r['K'] < r['N'],
    'UAN': lambda r: r['N'] >= 340,
    'Urea Ammonium Nitrate (UAN)': lambda r: r['N'] >= 340,
    'Urea Ammonium Nitrate (UAN)': lambda r: r['N'] >= 340,
    'DAP': lambda r: r['P'] >= 80,
    'SSP (Single Super Phosphate)': lambda r: r['P'] >= 60,
    'SSP': lambda r: r['P'] >= 60,
    'MOP (Potash)': lambda r: r['K'] >= 220,
    'Potassium Nitrate (KNO3)': lambda r: r['K'] >= 200 and r['N'] >= 100,
    'NPK 20-20-20': lambda r: abs(r['N']-r['P'])/max(1,r['N'])<0.12 and abs(r['P']-r['K'])/max(1,r['P'])<0.12,
    '14-35-14 (NPK)': lambda r: r['P']>=140 and r['N']>=120,
    '10-26-26 (NPK)': lambda r: r['P']>=120 and r['K']>=120,
    '17-17-17 (NPK)': lambda r: r['N']>=150 and r['P']>=150 and r['K']>=150,
    'Ammonium Sulphate': lambda r: r['N']>=200 and r['pH']<6.5,
    'Calcium Nitrate': lambda r: r['N']>=100 and r['pH']>=7.0,
    'Magnesium Sulphate': lambda r: r['N']<150 and r['K']<150 and r['pH']>=6.0,
    'Magnesium Nitrate': lambda r: r['N']>=150 and r['K']<100,
    'Zinc Sulphate': lambda r: r['N']<150 and r['P']<100 and r['K']<150,
    'Calcium Sulphate (Gypsum)': lambda r: r['pH']>7.0 and r['K']<150,
}

used_indices = set()
for fert in fert_list:
    found = None
    # try exact rule
    rule = rules.get(fert)
    if rule:
        for idx, row in df.iterrows():
            if idx in used_indices:
                continue
            try:
                if rule(row):
                    found = row.to_dict()
                    used_indices.add(idx)
                    break
            except Exception:
                continue
    results[fert] = found

# For any None results, pick the closest by heuristic distance: compute simple score
import math
for fert, res in list(results.items()):
    if res is not None:
        continue
    # fallback: pick row with max of a nutrient depending on fertilizer type
    if 'K' in fert or 'Potash' in fert:
        # choose row with highest K not used
        cand = df[~df.index.isin(used_indices)].sort_values('K', ascending=False).head(1)
    elif 'P' in fert or 'DAP' in fert or 'SSP' in fert:
        cand = df[~df.index.isin(used_indices)].sort_values('P', ascending=False).head(1)
    elif 'N' in fert or 'Urea' in fert or 'Ammonium' in fert:
        cand = df[~df.index.isin(used_indices)].sort_values('N', ascending=False).head(1)
    else:
        cand = df[~df.index.isin(used_indices)].head(1)
    if len(cand):
        idx = cand.index[0]
        results[fert] = cand.iloc[0].to_dict()
        used_indices.add(idx)
    else:
        results[fert] = None

# Print results as 17 input rows
out_lines = []
for fert in fert_list:
    r = results.get(fert)
    if r is None:
        out_lines.append((fert, 'No matching row found'))
    else:
        inp = {c: r[c] for c in ['region','soil_type','N','P','K','pH','temperature','humidity','rainfall','crop']}
        out_lines.append((fert, inp))

# Print
for fert, inp in out_lines:
    print('Fertilizer:', fert)
    print(inp)
    print()

# Also write to file
with open(proj / 'scripts' / 'fert_inputs_results.txt','w',encoding='utf-8') as f:
    for fert, inp in out_lines:
        f.write('Fertilizer: '+str(fert)+'\n')
        f.write(str(inp)+'\n\n')

print('Wrote scripts/fert_inputs_results.txt')
