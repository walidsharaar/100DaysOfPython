# Describe Problem
def my_function():
  for i in range(1, 20):
    if i == 20:
        # the range function upper bound is 19 and conditional statement will not print it.
        # for i in range(1, 21):
      print("You got it")

# the range function upper bound is 19 and conditional statement will not print it.
my_function()

# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# # dice_num = randint(0,5)
# # if rand int function calls 6 it will produce index out range error
# print(dice_imgs[dice_num]

# Play Computer
year= int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
# both conditional statement dont covers 1994
# elif year>=1994 or year<=1994
elif year > 1994:
  print("You are a Gen Z.")


# Fix the Errors
age = int(input("How old are you?"))
#age value is string and have to convert in int.
if age > 18:
# it is not indented and fstring is needed in the print statement
    print(f"You can drive at age {age}.")


#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# the below statement is incorrect and it is comparing.
# it is the correct format word_per_page = int(input("Number of words per page: "))

word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  #append it outside of the loop
  #  b_list.append(new_item)
  b_list.append(new_item)
  print(b_list)



mutate([1,2,3,5,8,13])