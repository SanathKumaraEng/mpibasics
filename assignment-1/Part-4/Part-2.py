from mpi4py import MPI
import csv

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

NUM_SUBJECTS = 4

# Initialize variables
local_sums = [0] * NUM_SUBJECTS
local_counts = [0] * NUM_SUBJECTS
local_avg = [0] * NUM_SUBJECTS

# Read grades from CSV file
with open('grades.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    
    # Skip header row
    next(reader)
    
    # Divide the work among processes
    rows = list(reader)
    num_rows = len(rows)
    rows_per_process = num_rows//size

    # Divide rows among processes based on rank
    start = rank * rows_per_process
    end = (rank+1) * rows_per_process

    
    if (rank == size-1 and end < num_rows):
        end = num_rows + 1

    local_rows = rows[start:end]

# Calculate local sums, counts, and averages
for row in local_rows:
    for i in range(NUM_SUBJECTS):
        grade = int(row[i])
        local_sums[i] += grade
        local_counts[i] += 1
        local_avg[i] = local_sums[i] / local_counts[i]

# Gather local averages from all processes to process 0
all_sums = comm.gather(local_sums, root=0)
global_counts = comm.gather(local_counts, root=0)

if rank == 0:
    # Process 0 receives the gathered averages
    for i in range(NUM_SUBJECTS):
        subject_sums = [sum[i] for sum in all_sums]
        global_count = [count[i] for count in global_counts]
        subject_avg = sum(subject_sums)/sum(global_count)
        if (i==0):
            print("Mathematics:", subject_avg)
        if (i==1):
            print("English:", subject_avg)
        if (i==2):
            print("Data Structures and Algorithms:", subject_avg)
        if (i==3):
            print("High Performance Computing:", subject_avg)