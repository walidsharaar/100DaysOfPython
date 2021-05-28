'''
You are going to write a program which will select a random name from a list of names.
The person selected will have to pay for everybody's food bill.
Important: You are not allowed to use the choice() function.
Line 8 splits the string names_string into individual names and puts them inside a List called names.
For this to work , you must enter all the names as name followed by comma then space. e.g. name, name, name
'''
import random

# create a list

name_input = input("Enter all names in comma separated format: ")
name = name_input.split(",")

pay_bill= random.randint(0,len(name)-1)

print(f"You are the lucky person {name[pay_bill]} to pay the bill today!")