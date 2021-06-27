
weather_list = []

with open("weather_data.csv") as weather:
    weathers=weather.readlines()
    print(weathers)