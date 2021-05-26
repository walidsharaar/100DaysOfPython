
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

