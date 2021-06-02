'''
Prime numbers are numbers that can only be cleanly divided by itself and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

https://cdn.fs.teachablecdn.com/s0gceS97QD6MP5RUT49H

Here are the numbers up to 100, prime numbers are highlighted in yellow:

https://cdn.fs.teachablecdn.com/NZqVclSt2qAe8KhTsUtw

Example Input 1
73
Example Output 1
It's a prime number.
Example Input 2
75
Example Output 2
It's not a prime number.

'''

print("Welcome to prime number checker")

def prime_checker(prime_number):
    is_prime = True
    for i in range(2,prime_number):
        if prime_number % i == 0:
                is_prime = False
    if is_prime:
        print("It is  a prime number.")
    else:
        print("It is a not a prime number ")



prime_checker (int(input("Check this number: ")))
