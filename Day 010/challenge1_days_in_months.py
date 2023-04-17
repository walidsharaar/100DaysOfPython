'''
In the starting code, you'll find the solution from the Leap Year challenge.
First, convert this function is_leap() so that instead of printing "Leap year."
or "Not leap year." it should return True if it is a leap year and return False if it is
not a leap year.
You are then going to create a function called days_in_month() which will take a year
and a month as inputs, e.g.
days_in_month(year=2022, month=2)
And it will use this information to work out the number of days in the month,
then return that as the output, e.g.:
28
The List month_days contains the number of days in a month from January to December
for a non-leap year. A leap year has 29 days in February.
Hint
Look at the function call at the bottom of the code to see the positional arguments.
The order is very important.
Feel free to choose your own parameter names.
Remember that month_days is a List and Lists in Python start at position 0.
So the number of days in January is month_days[0]
Be careful with indentation.
'''

# create days functions

def days_in_month(the_year, the_month):
    is_leap = False
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_name =  ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']

    #check for leap year

    if the_year % 4 == 0:
        if the_year % 100 == 0:
            if the_year % 400 == 0:
                month_days[1]=29
                is_leap=True
            else:
                month_days[1] = 29
                is_leap = True
        dis_day = month_days[the_month-1]
        dis_month = month_name[the_month-1]
        if is_leap is True:
            print(f"{the_year} is a leap year. There are {dis_day} days in {dis_month}.")
        else:
            print(f"{the_year} is a leap year. There are {dis_day} days in {dis_month}.")

year=int(input("Enter the year: "))
month=int(input("Enter the month number: "))

days_in_month(year, month)


