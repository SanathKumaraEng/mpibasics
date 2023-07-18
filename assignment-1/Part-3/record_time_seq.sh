#!/bin/bash

# CSV file path
csv_file="execution_times_seq.csv"

# Record the start time
start_time=$(date +%s.%N)

# Run your Python script
python Part-1.py

# Record the end time
end_time=$(date +%s.%N)

# Calculate the execution time
execution_time=$(echo "$end_time - $start_time" | bc)

# Print the execution time
echo "Execution time: $execution_time seconds"

# Append the execution time to the CSV file
echo "$execution_time" >> "$csv_file"
