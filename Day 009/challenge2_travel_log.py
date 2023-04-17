'''
You are going to write a program that adds to a travel_log.
You can see a travel_log which is a List that contains 2 Dictionaries.
Write a function that will work with the following line of code on line 21 to add
the entry for Russia to the travel_log.
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
You've visited Russia 2 times.
You've been to Moscow and Saint Petersburg.
DO NOT modify the travel_log directly. You need to create a function that modifies it.
'''

# Todo 1: Create list of the travel log

travel_log = [
{
  "name": "France",
  "visits": 1,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "name": "Germany",
  "visits": 1,
  "cities": ["Berlin", "Hamburg", "Munich"]
},
]
print(travel_log)
#todo write the function to  add other countries

def add_country(country_visited,number_visited,cities_visited):

    #create a new list of the country
    new_country={}

    new_country["name"]= country_visited
    new_country["visities"] = number_visited
    new_country["cities"] = cities_visited

    #add all items
    travel_log.append(new_country)
add_country("Afghanistan",4,["Kabul","Balkh","Herat"])
print(travel_log)