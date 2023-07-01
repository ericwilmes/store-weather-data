import json
import requests

def save_weather_data(weather_data, file_path):
    try:
        with open(file_path, "r") as f:
            existing_data = json.load(f)
    except:
        existing_data = {
            "observations": [],
        }

    for new_data in weather_data["observations"]:
        if new_data not in existing_data["observations"]:
            existing_data["observations"].append(new_data)

    with open(file_path, "w") as f:
        json.dump(existing_data, f)

api_key = "0178ccfd8eeb43cbb8ccfd8eebb3cb43"
station_id = "KCOCOLOR2562"
one_day_url = f"https://api.weather.com/v2/pws/observations/all/1day?stationId={station_id}&format=json&units=e&apiKey={api_key}"

# Get weather data
response = requests.get(one_day_url)
weather_data = response.json()
save_weather_data(weather_data, "weather_data.json")
