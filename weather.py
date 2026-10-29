import csv
import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 10.91,      # Tirur
    "longitude": 75.92,
    "daily": "temperature_2m_max,precipitation_sum",
    "timezone": "Asia/Kolkata",
}

response = requests.get(url, params=params, timeout=10)
response.raise_for_status()
data = response.json()["daily"]

with open("weather.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "max_temp_c", "rain_mm"])
    for d, t, r in zip(data["time"], data["temperature_2m_max"], data["precipitation_sum"]):
        writer.writerow([d, t, r])

print("Saved weather.csv")