# import csv
#
# with open("weather_data.csv") as data_file:
#     data= csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas

data =pandas.read_csv("weather_data.csv")
# print(type(data))
# temp=data["temp"]
# print(temp)
data_dict = data.to_dict()
print(data_dict)
data_list = data["temp"].to_list()
print(data["temp"].mean())

print(data_list)

#data in columns
print(data["condition"])


