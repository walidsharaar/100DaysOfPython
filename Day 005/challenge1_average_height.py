'''
You are going to write a program that calculates the average student height
 from a List of heights.
e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
The average height can be calculated by adding all the heights together
and dividing by the total number of heights.
e.g.
180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
There are a total of 7 heights in student_heights
1146 ÷ 7 = 163.71428571428572
Average height rounded to the nearest whole number = 164
Important You should not use the sum() or len() functions in your answer.
You should try to replicate their functionality using what you have learnt about for loops.

'''

# Receiving students height

student_heights = input("Enter the heights:\n").split()

#loop the student to store the input intp a list

for student_height in range(0,len(student_heights)):
    student_heights[student_height] = int (student_heights[student_height])


# first we have find the Total of height
total_height = 0
for height in student_heights:
    total_height+=height
print(f"Total height of the students are:{total_height}")

student_count = 0

for student in student_heights:
    student_count+=1

print(f"Number of the students are: {student_count}")

print(student_height/student_count)
