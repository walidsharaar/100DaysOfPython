'''
Write a program that works out whether if a given year is a leap year.
A normal year has 365 days,leap years have 366, with an extra day in February.

'''

year = int(input("Enter a year : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year!")
        else:
            print("It is a not leap year!")
    else:
        print("It is a leap year!")
else:
    print("It is not a leap year!")
