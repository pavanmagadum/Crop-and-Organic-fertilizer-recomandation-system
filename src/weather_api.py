import requests, pandas as pd
def fetch_weather(region, api_key=None):
    if api_key:
        try:
            url = f'http://api.openweathermap.org/data/2.5/forecast?q={region}&appid={api_key}&units=metric'
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            data = r.json()
            temps = [item['main']['temp'] for item in data.get('list',[])]
            hums = [item['main']['humidity'] for item in data.get('list',[])]
            rain = 0.0
            for it in data.get('list',[]):
                rain += it.get('rain',{}).get('3h',0.0)
            return {'avg_temp': sum(temps)/len(temps) if temps else None, 'avg_humidity': sum(hums)/len(hums) if hums else None, 'rainfall_est': rain, 'simulated':False}
        except Exception as e:
            pass
    try:
        df = pd.read_csv('data/crop_data.csv')
        return {'avg_temp': df['temperature'].mean(), 'avg_humidity': df['humidity'].mean(), 'rainfall_est': df['rainfall'].mean(), 'simulated':True}
    except Exception as e:
        return {'avg_temp':25.0,'avg_humidity':70.0,'rainfall_est':600.0,'simulated':True}
