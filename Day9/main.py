#dictionary
# {"key":"value"}

#defining dictionary

content={
    "name":"walid",
    "f_name":"Asad"}

#printing dictionary

print(content["name"])

# adding item to the dictionary

content["age"] ="18"

print(content)

#edit item of the dictionary

content["age"]= "20"

print(content)

#loop throug a dictionary

for key in content:
    print(key)
    print(content[key])

#nesting in dictionaries
#{key:[list],key2:{Dict}}

capitals ={
    "France": "Paris",
    "Germany":"Berlin",
    "Afghanistan":"Kabul"
}
print(capitals)

# nest list in a dictionary

visit_cities={
    "France":["paris"],
    "Austria":["Linz"],
    "Turkey":["Izmir","Istanbul","Ankara"],
    "Afghanistan":["Kabul","Balk"]
}

print(visit_cities)


# nest dictionary into dictionary

cities={
    "France":{"cities_visited":["paris","Dijon"]},
    "Austria":["Linz"],
    "Turkey":["Izmir","Istanbul","Ankara"],
    "Afghanistan":["Kabul","Balk"]
}

print(cities)