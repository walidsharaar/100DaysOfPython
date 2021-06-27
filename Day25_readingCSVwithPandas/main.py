import csv
weather_list = []

with open("weather_data.csv") as weather:
    weathers= csv.reader(weather)
    for row in weathers:
        print(row)

