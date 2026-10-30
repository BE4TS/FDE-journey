import csv
import requests

url = "https://api.open-meteo.com/v1/forecast"
def fetch_data(lat,lng):
    params = {
    "latitude": lat,      # Tirur
    "longitude": lng,
    "daily": "temperature_2m_max,precipitation_sum",
    "timezone": "Asia/Kolkata",
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.ConnectionError:
        print("No internet connection ")
        raise SystemExit(1)
    except requests.Timeout:
        print("The server took long to respond  ")
        raise SystemExit(1)
    except requests.RequestException as e:
        print(f"Request failed: {type(e).__name__}")
        raise SystemExit(1)
    return response.json()["daily"]



def save_csv(data,filename="weather.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "max_temp_c", "rain_mm"])
        for d, t, r in zip(data["time"], data["temperature_2m_max"], data["precipitation_sum"]):
            writer.writerow([d, t, r])


data=fetch_data(10.91,75.92)
save_csv(data)
print("saved weather.csv")
