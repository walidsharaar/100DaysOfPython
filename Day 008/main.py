# input functions in python

def my_function(name,location):

    print(f"Greeting form a function {name} !")
    print(f"How do you do {name}? ")
    print(f"{name} isn't the weather nice today in {location}?")
    
my_function(input("Enter your name:\n"),"")



# using of keyword arguments

my_function(name=input("Enter your name:"),location=input("Enter the location:"))
