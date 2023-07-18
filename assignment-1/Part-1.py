import csv

# Initialize variables
subject_averages = [0] * 4
num_students = 0

# Read grades from CSV file
with open('grades.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    
    # Skip header row
    next(reader)
    
    # Iterate over each student's grades
    for row in reader:
        for i in range(len(row)):
            # Convert grade to integer
            grade = int(row[i])
            
            # Accumulate grades for each subject
            subject_averages[i] += grade
        
        num_students += 1

# Calculate averages
for i in range(len(subject_averages)):
    subject_averages[i] /= num_students

# Display averages
print("Subject Averages:")
print("Mathematics:", subject_averages[0])
print("English:", subject_averages[1])
print("Data Structures and Algorithms:", subject_averages[2])
print("High Performance Computing:", subject_averages[3])

