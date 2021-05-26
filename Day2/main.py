#Data Types

#String
print("Hello"[4])
#Integer
print(123+234)
#float
print(3.13159)
#boolean
True
False


num_char = len(input("Enter your name?"))
print(num_char)
# check the type of variable

print(type(num_char))

new_num_char = str(num_char)

print("Your name has " + new_num_char +" characters.")


'''
Challenge Number 1 of day 2
Instructions
Write a program that adds the digits in a 2 digit number. 
e.g. if the input was 35, then the output should be 3 + 5 = 8
Warning. Do not change the code on lines 1-3. 
Your program should work for different inputs. 
e.g. any two-digit number.
Hint
Try to find out the data type of two_digit_number.
Think about what you learnt about subscripting.
Think about type conversion.

'''

input_digit = input("Enter a two digit number please:\n")
first_digit= int(input_digit[0])
second_digit=int(input_digit[1])
print(first_digit+second_digit)






