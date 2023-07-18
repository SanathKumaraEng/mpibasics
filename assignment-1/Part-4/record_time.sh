#!/bin/bash

##### Recording time to run sequential program (Part-1.py) #####
# CSV file path
csv_file_seq="execution_times_seq.csv"

# Record the start time
start_time_seq=$(date +%s.%N)

# Run your Python script
python Part-1.py

# Record the end time
end_time_seq=$(date +%s.%N)

# Calculate the execution time
execution_time_seq=$(echo "$end_time_seq - $start_time_seq" | bc)

# Print the execution time
echo "Execution time: $execution_time_seq seconds"

# Append the execution time to the CSV file
echo "$execution_time_seq" >> "$csv_file_seq"



##### Recording time to run mpi program (Part-2.py) #####
# CSV file path
csv_file_mpi="execution_times_mpi.csv"

# Record the start time
start_time_mpi=$(date +%s.%N)

# Run your Python script
mpirun -n 4 python3 Part-2.py

# Record the end time
end_time_mpi=$(date +%s.%N)

# Calculate the execution time
execution_time_mpi=$(echo "$end_time_mpi - $start_time_mpi" | bc)

# Print the execution time
echo "Execution time: $execution_time_mpi seconds"

# Append the execution time to the CSV file
echo "$execution_time_mpi" >> "$csv_file_mpi"
