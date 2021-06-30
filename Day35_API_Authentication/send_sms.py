import requests
from twilio.rest import Client
API_KEY= "94d611536bbb1ddde200017784621c27"
OWM_ENDPOINT="https://api.openweathermap.org/data/2.5/onecall"
LAT=52.5244
LONG=13.4105

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC60595cef50f52688c7bdec2112342600"
auth_token = "29b4e769ffe4a6f85cac561c0854c282"

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
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="it is raining. Have an umbrella.",
        from_='+15392860952',
        to='Your Verified Number '
    )
    print(message.status)
