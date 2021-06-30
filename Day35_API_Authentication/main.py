import requests

API_KEY= "94d611536bbb1ddde200017784621c27"
OWM_ENDPOINT="https://api.openweathermap.org/data/2.5/onecall"
LAT=52.5244
LONG=13.4105
weather_params={
    "lat":LAT,
    "lon":LONG,
    "appid":API_KEY,
    "exclude":"current,minutely,daily"
}

#current weather

response = requests.get(OWM_ENDPOINT,params=weather_params)
response.raise_for_status()
weather_data=response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    connection_code= hour_data["weather"][0]["id"]
    if int(connection_code)<700:
        will_rain=True
if will_rain:
        print("Bring an umbrella.")
# print(weather_data["hourly"][0]["weather"][0]["id"])