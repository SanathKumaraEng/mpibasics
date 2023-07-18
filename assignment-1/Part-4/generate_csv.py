import csv
import random

NUM_STUDENTS = 5000000
NUM_SUBJECTS = 4
MAX_GRADE = 100

# Generate random grades for each student and each subject
grades = []
for _ in range(NUM_STUDENTS):
    student_grades = []
    for _ in range(NUM_SUBJECTS):
        grade = random.randint(0, MAX_GRADE)
        student_grades.append(grade)
    grades.append(student_grades)

# Write grades to a CSV file
with open('grades.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Mathematics', 'English', 'Data Structures and Algorithms', 'High Performance Computing'])
    for student_grades in grades:
        writer.writerow(student_grades)

print("Grades have been generated and saved to grades.csv.")
