#list comprehension
# new_list = [new_item for item in list]

#normal list
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