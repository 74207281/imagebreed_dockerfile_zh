'''
Export html file for showing weather of sepecific filed
'''

import requests
import datetime

# Get Data From CWA Opendata API
def get_response(url,params):
    response = requests.get(url, params=params, headers={'accept': 'application/json'})
    if not 200 <= response.status_code < 300:
        raise RuntimeError("Failed to retrieve CWA weather data.")
    return response.json()

# Parse CWA Data
def parse_cwa_current_data(data):
    if data is None:
        raise RuntimeError("Failed to retrieve CWA weather data.")
    date = data['records']['Station'][0]['ObsTime']['DateTime']
    station_name = data['records']['Station'][0]['StationName']
    obs_date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")
    weather_elements = data['records']['Station'][0]['WeatherElement']
    weather = weather_elements['Weather']
    temperature = weather_elements['AirTemperature']
    humidity = weather_elements['RelativeHumidity']
    pressure = weather_elements['AirPressure']
    precipitation = weather_elements['Now']['Precipitation']
    wind_direction = weather_elements['WindDirection']
    wind_speed = weather_elements['WindSpeed']
    cwa_current = {
        'Name': station_name,
        'ObsevationTime': obs_date.strftime("%Y-%m-%d %H:%M:%S"),
        'Weather': weather,
        'Temperature': temperature,
        'Humidity': humidity,
        'AirPressure': pressure,
        'Precipitation': precipitation,
        'WindDirection': wind_direction,
        'WindSpeed': wind_speed
    }
    return cwa_current

def parse_cwa_past_data(data):
    if data is None:
        raise RuntimeError("Failed to retrieve CWA past weather data.")
    # Find correct station:
    station_name = data['records']['location'][0]['station']['StationName']
    date_lenght = len(data['records']['location'][0]['stationObsTimes']['stationObsTime'])
    cwa_past = []
    for i in range(date_lenght):
        data_date = datetime.datetime.strptime(
            data['records']['location'][0]['stationObsTimes']['stationObsTime'][i]['DateTime'], 
            "%Y-%m-%dT%H:%M:%S%z")
        date = data_date.strftime("%Y-%m-%d %H:%M:%S")
        weather_elements = data['records']['location'][0]['stationObsTimes']['stationObsTime'][i]['weatherElements']
        temperature = weather_elements['AirTemperature']
        humidity = weather_elements['RelativeHumidity']
        pressure = weather_elements['AirPressure']
        precipitation = weather_elements['Precipitation']
        wind_direction = weather_elements['WindDirection']
        wind_speed = weather_elements['WindSpeed']
        Sunshine = weather_elements['SunshineDuration']
        cwa_past.append({
            'Name': station_name,
            'Date': date,
            'Temperature': temperature,
            'Humidity':humidity,
            'AirPressure': pressure,
            'Precipitation': precipitation,
            'WindDirection': wind_direction,
            'WindSpeed': wind_speed,
            'SunshineDuration': Sunshine
        })
    
    return cwa_past

# Return HTHL file
def get_current_html_file(current_data):
    try: 
        with open('weather.html' , 'w') as file:
            file.write('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Data</title>
    <style>
        .weather-container {
            font-family: Arial, sans-serif;
            border: 1px solid #ccc;
            padding: 20px;
            border-radius: 8px;
            max-width: 400px;
            margin: 20px auto;
            background-color: #f9f9f9;
        }
        .weather-item {
            margin-bottom: 10px;
            display: flex;
            justify-content: space-between;
        }
        .label {
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="weather-container">''')
            for key, value in current_data.items():
                file.write(f'''
        <h2>{key}</h2>
        <div class="{key}-item">
            <span>{value}</span>
        </div>''')
            file.write('''
    </div>
</body>
</html>
    ''')
            return None
    except Exception as e:
        raise RuntimeError("Failed to retrieve CWA weather data.")

# if __name__ == '__main__':
#     try:
#         current_respond = get_response(current_url, CWA_API_TOKEN, )
#         data = parse_cwa_current_data(current_respond)
#         get_current_html_file(data)
#     except Exception as e:
#         print(e)

