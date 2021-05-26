
'''
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and
a short person both weigh the same amount, the short person is usually more overweight.

'''
print("Welcome!!\n")

weight=input("Enter the weight in kg:\n")
height=input("Enter the height in m:\n")

weight_int = int(weight)
height_float= float(height)
bmi= weight_int/(height_float*height_float)
print(int(bmi))


