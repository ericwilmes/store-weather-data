import json
import requests
from git import Repo


def save_weather_data(weather_data, file_path):
    with open(file_path, "w") as f:
        json.dump(weather_data, f)


def commit_and_push(file_path, repo):
    repo.index.add("/" + file_path)
    repo.index.commit("Update weather data")
    origin = repo.remote(name="origin")
    origin.push()


api_key = "0178ccfd8eeb43cbb8ccfd8eebb3cb43"
station_id = "KCOCOLOR2562"
one_day_url = f"https://api.weather.com/v2/pws/observations/all/1day?stationId={station_id}&format=json&units=e&apiKey={api_key}"

# Get weather data
response = requests.get(one_day_url)
weather_data = response.json()
save_weather_data(weather_data, "weather_data.json")

repo = Repo.init("store-weather-data")
origin = repo.remote("origin")
commit_and_push("weather_data.json", repo)
