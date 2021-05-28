# Usage of random module

import random

random_integer= random.randint(1,10)

print(random_integer)

# 0.0000 to 0.999999
random_float = random.random()
print(random_float)

# lists in python

fruits = ['Grapes', 'Guava', 'Apricots' , 'Cantaloupe','Bananas','Oranges','Mangoes']

print(f"Today you have to eat "+ random.choice(fruits))
