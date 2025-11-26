from pytube import Search
import pandas as pd
from pytube import Search
import os
def load_mapping(path='data/fertilizer_mapping.csv'):
    return pd.read_csv(path)
def convert_non_to_org(nonorganic, mapping_df=None):
    if mapping_df is None:
        mapping_df = load_mapping()
    row = mapping_df[mapping_df['nonorganic'].str.lower() == str(nonorganic).lower()]
    def _prep_to_list(val):
        if pd.isna(val):
            return []
        # split on semicolon or newline, strip
        parts = [p.strip() for p in str(val).split(';') if p.strip()]
        return parts

    if len(row):
        r = row.iloc[0].to_dict()
        prep = _prep_to_list(r.get('preparation', ''))
        return {
            'nonorganic': r.get('nonorganic', nonorganic),
            'organic': r.get('organic', 'Vermicompost'),
            'notes': r.get('notes', ''),
            'preparation_steps': prep
        }
    first = mapping_df.iloc[0].to_dict()
    prep = _prep_to_list(first.get('preparation', ''))
    return {
        'nonorganic': nonorganic,
        'organic': first.get('organic', 'Vermicompost'),
        'notes': first.get('notes', ''),
        'preparation_steps': prep
    }
def fetch_tutorials_pytube(query, max_results=5):
    try:
        s = Search(f"{query} organic fertilizer tutorial")
        results = s.results[:max_results]
        out = []
        for r in results:
            out.append({'title': r.title, 'link': r.watch_url})
        return out
    except Exception as e:
        return [{'title':'pytube error','link':str(e)}]
def fetch_tutorials_youtube_api(query, api_key, max_results=5):
    try:
        import requests
        url = 'https://www.googleapis.com/youtube/v3/search'
        params = {'part':'snippet','q':query+' organic fertilizer tutorial','key':api_key,'maxResults':max_results,'type':'video'}
        r = requests.get(url, params=params, timeout=10)
        items = r.json().get('items',[])
        out = []
        for it in items:
            title = it['snippet']['title']
            vid = it['id']['videoId']
            out.append({'title':title,'link':f'https://www.youtube.com/watch?v={vid}'})
        return out
    except Exception as e:
        return [{'title':'youtube api error','link':str(e)}]


def build_search_queries(organic_name):
    """Return a prioritized list of search query strings for an organic fertilizer name.

    Adds domain-specific terms so searches find preparation/tutorial videos.
    """
    name = str(organic_name or '').lower()
    queries = []
    base = f"how to prepare {name}"
    queries.append(base)

    # Add domain-specific keywords
    if 'vermi' in name or 'vermicompost' in name:
        queries.append(f"vermicompost extract preparation {name}")
        queries.append(f"how to make vermicompost tea {name}")
    if 'compost' in name or 'compost tea' in name:
        queries.append(f"compost tea recipe {name}")
        queries.append(f"how to brew compost tea for {name}")
    if 'jivamrutha' in name or 'cow dung' in name:
        queries.append(f"jivamrutha preparation {name}")
        queries.append(f"fermented cow dung solution recipe {name}")
    if 'banana' in name or 'banana peel' in name:
        queries.append(f"banana peel fertilizer recipe {name}")
    # generic fallback variations
    queries.append(f"organic fertilizer preparation {name}")
    queries.append(f"homemade {name} fertilizer tutorial")
    # dedupe preserving order
    seen = set(); out = []
    for q in queries:
        if q not in seen:
            out.append(q); seen.add(q)
    return out


def predict_fertilizer_simple(N, P, K, pH=None, crop=None):
    """Simple heuristic to predict a non-organic fertilizer type based on N/P/K levels.

    Rules (simple):
    - If N is dominant -> 'Urea' or 'UAN'
    - If P is dominant -> 'DAP' or 'SSP'
    - If K is dominant -> 'MOP (Potash)'
    - If balanced -> 'NPK 20-20-20'
    - Adjust for very low/very high pH or specific crops (basic examples)
    """
    try:
        vals = {'N': float(N), 'P': float(P), 'K': float(K)}
    except Exception:
        return 'NPK 20-20-20'
    maxnut = max(vals, key=vals.get)
    # basic crop-based overrides
    crop = (str(crop).lower() if crop else '')
    if crop in ('rice','sugarcane'):
        # heavy N and K feeders
        if vals['K'] > vals['N']:
            return 'MOP (Potash)'
        return 'Urea'
    if maxnut == 'N':
        return 'Urea'
    if maxnut == 'P':
        return 'DAP'
    if maxnut == 'K':
        return 'MOP (Potash)'
    return 'NPK 20-20-20'


def build_search_queries(organic):
    """Generate prioritized search queries for tutorial videos based on organic fertilizer name.

    Returns a list of query strings ordered from most-specific to broader queries.
    """
    if not organic:
        return ['how to prepare organic fertilizer', 'organic fertilizer tutorial']
    # take primary name (before comma) and strip
    primary = str(organic).split(',')[0].strip()
    base = primary.lower()
    queries = []
    # specific recipe/prep names
    queries.append(f'how to prepare {base} organic fertilizer')
    queries.append(f'{base} preparation tutorial')
    queries.append(f'{base} organic fertilizer recipe')
    # include common related keywords
    queries.append(f'{base} compost tea preparation')
    queries.append(f'{base} vermicompost extract tutorial')
    queries.append(f'how to make {base} at home')
    # fallbacks
    queries.append(f'{base} organic fertilizer tutorial')
    queries.append('how to prepare organic fertilizer')
    # dedupe while preserving order
    seen = set(); out = []
    for q in queries:
        if q not in seen:
            out.append(q); seen.add(q)
    return out
