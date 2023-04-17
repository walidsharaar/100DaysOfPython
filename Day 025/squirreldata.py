'''
The Squirrel Census (https://www.thesquirrelcensus.com/) is a multimedia science, design, and storytelling project focusing on the Eastern gray (Sciurus carolinensis).
They count squirrels and present their findings to the public.
This table contains squirrel data for each of the 3,023 sightings,
including location coordinates, age, primary and secondary fur color,
elevation, activities, communications, and interactions between squirrels and with humans.

link : https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw
'''

import pandas

data=pandas.read_csv("squirrel_data.csv")
grey_squirrel=data[data["Primary Fur Color"] == "Gray"]
grey_squirrel_count = len(data[data["Primary Fur Color"]=="Gray"])
red_squirrel_count=data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrel_count = len(data[data["Primary Fur Color"]=="Black"])
print(grey_squirrel)
print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict ={
    "Color" : ["Gray","Cinnamon","Black"],
    "Count" : [grey_squirrel_count,red_squirrel_count,black_squirrel_count]
}
df=pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")

print(data_dict)