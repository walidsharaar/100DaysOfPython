'''
 Your job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
Example Input
size = "L"
add_pepperoni = "Y"
extra_cheese = "N"
Example Output
Your final bill is: $28.
'''

print("Welcome to your shop!")
size=input("Please select your pizza size S,M or L\n")
add_pepperoni =input("If you want to add pepperoni enter Y for yes and N for no\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
bill = 0
if size == "S":
    bill = 15
elif size =="M":
    bill +=20
else:
    bill +=25
if add_pepperoni == "Y":
    if size =="s":
     bill +=2
else:
    bill += 3
if extra_cheese == "Y":
    bill += 3
    print(f"Your bill is $ {bill}")
