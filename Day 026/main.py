#list comprehension
# new_list = [new_item for item in list]

#normal list
import random

numb= [1,2,3]
new_list =[]
for n in numb:
    add_1 = n+1
    new_list.append(add_1)
print(new_list)

# list comprehension

name="Khwaja Walid Sharaar"
new_list = [letter for letter in name]
print(new_list)

num_list = [number*2 for number in range(1,5)]
print(num_list)

# conditional list comprehension
#new_list = [new_item for item in list if test]

names=["Alex","Beth","Dave","Carolina","Eleanor","Freddie"]
new_name = [name for name in names if len(name) < 5]
print(new_name)

capital_name = [name.upper() for name in names if len(name) < 5]
print(capital_name)

# dictionary comprehension
# new_dict ={new_key:new_value for item in list}

students_score = {student: random.randint(1,100) for student in names}
print(students_score)

#new_dict = {new_key:new_value for (key,value) in dictionary.items()}
passed_student = {student:score for(student,score) in students_score.items() if score>=60 }
print(passed_student)