'''
You are going to write a program which will mark a spot with an X.
In the starting code, you will find a variable called map.
This map contains a nested list.
When map is printed this is what the nested list looks like:
['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
In the starting code, we have used new lines (\n) to format the three rows into a square,
like this:
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
Your job is to write a program that allows you to mark a square on
the map using a two-digit system. The first digit is the vertical
column number and the second digit is the horizontal row number.
'''

# Rows creation
first_row =["🏽","🏽","🏽"]
second_row =["🏽","🏽","🏽"]
third_row =["🏽","🏽","🏽"]

# Map creation
map_creation =[first_row,second_row,third_row]

print(f"{first_row}\n{second_row}\n{third_row}")

user_input = input("Where do you wanna put the treasure?\n")

#identifying the positions

horizonal_position = int(user_input[0])
vertical_position =int (user_input[1])
map_creation[vertical_position-1][horizonal_position-1] = "W"

#Printing the final output
print(f"{first_row}\n{second_row}\n{third_row}")


