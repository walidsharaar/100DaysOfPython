
# program started

print("Welcome Stranger!!!")

height = int(input("Please enter your height"))
bill=0

if height>=120:
    print("Enjoy your ride!")
    age = int(input("Please enter your age"))
    if age <12 :
        bill = 5
        print("Your ticket cost $5")
    elif age <=18:
        bill = 7
        print("Your ticket cost $7")
    elif age >= 45 and age <=55:
        print("You can ride without any cost")
    else:
        bill=12
        print("Your ticket cost $12")
    photo = input("Do you want to take photo? Y or N")
    if photo == "y" :
        bill +=3
    print(f"Your ticket cost is ${bill}")
else:
    print("You are not eligible to ride!")