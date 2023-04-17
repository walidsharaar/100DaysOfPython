'''
You have access to a database of student_scores in the format of a dictionary.
The keys in student_scores are the names of the students and the values are their exam scores.

Write a program that converts their scores to grades. By the end of your program,
you should have a new dictionary called student_grades that should contain student names
for keys and their grades for values. The final version of the student_grades dictionary will be checked.

DO NOT modify lines 1-7 to change the existing student_scores dictionary.

DO NOT write any print statements.

This is the scoring criteria:

Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"

Expected Output
'{'Harry': 'Exceeds Expectations',
 'Ron': 'Acceptable',
 'Hermione': 'Outstanding',
 'Draco': 'Acceptable',
  'Neville': 'Fail'}'
'''

print("Welcome to grading system!")

student_score = {"A":81,
                 "B":91,
                 "C":50,
                 "D":62,
                 "E":74}
#Todo 1 - create a empty dictionary
student_grade ={}
#Todo 2 - write the code about the grading

for key in student_score:
    score = student_score[key]

    if score >90 :
        student_grade[key]="outstanding"
    elif score > 80:
        student_grade[key] = "Good"
    elif score > 70:
        student_grade[key] = "Acceptable"
    elif score >50 :
        student_grade[key]="Pass"
    else:
        student_grade[key]="fail"

print(student_grade)