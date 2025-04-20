from dotenv import load_dotenv
import os
import requests
import time

load_dotenv()

api_key = os.getenv("API_KEY")


def retry(func):
    def wrapper_retry(*args, **kwargs):
        retries = [5, 30]
        for seconds in retries:
            try:
                return func(*args, **kwargs)
            except requests.exceptions.RequestException:
                print(f"Failed to get data. Retrying in {seconds} seconds")
                time.sleep(seconds)
        return func(*args, **kwargs)
    return wrapper_retry


@retry
def get_weather_by_hours_for_day_from_api(*, date: str, city: str) -> list[dict]:
    res = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date}/{date}?unitGroup=us&key={api_key}")
    result = res.json()
    weather_by_days = result["days"]
    weather_bu_hours = weather_by_days[0]["hours"]
    return weather_bu_hours


def fahrenheit_to_celsius(*, fahrenheit_temp: float) -> int:
    return round((fahrenheit_temp - 32) * 5 / 9)


def get_dangerous_hours(*, hours: list[dict]) -> list[dict]:
    dangerous_hours = []
    for weather in hours:
        uvindex = weather["uvindex"]
        time = weather["datetime"]
        celsius_temp = fahrenheit_to_celsius(fahrenheit_temp=weather["temp"])
        if uvindex >= 3:
            dangerous_hours.append({"time": time, "uvindex": uvindex, "temp": celsius_temp})
    return dangerous_hours

weather_by_hours = get_weather_by_hours_for_day_from_api(date="2025-04-19", city="Reykjavik")

dangerous_hours = get_dangerous_hours(hours=weather_by_hours)
print(dangerous_hours)