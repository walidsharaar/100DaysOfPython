import requests

API_KEY= "94d611536bbb1ddde200017784621c27"
OWM_ENDPOINT="https://api.openweathermap.org/data/2.5/onecall"
LAT=52.5244
LONG=13.4105
weather_params={
    "lat":LAT,
    "lon":LONG,
    "appid":API_KEY,
}

#current weather

response = requests.get(OWM_ENDPOINT,params=weather_params)
print(response.json())