import csv
import hashlib
from mpi4py import MPI

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Define the path to the CSV file
csv_file_path = 'data.csv'

# Define the path to the search query file
search_query_file = 'search_queries.txt'

# Read the rows from the search query file and convert them to hash values
rows_to_search = []
with open(search_query_file, 'r') as query_file:
    for line in query_file:
        row_values = line.strip().split(',')
        hash_values = [hashlib.sha256(value.encode()).hexdigest() for value in row_values]
        rows_to_search.append(hash_values)

# Calculate the number of records per process
total_records = 1000000
records_per_process = total_records // size

# Calculate the start and end indices for the current process
start_index = rank * records_per_process
if start_index != 0:
    start_index += 1

end_index = (rank + 1) * records_per_process

# Open the CSV file
with open(csv_file_path, 'r') as csv_file:
    # Create a CSV reader object
    reader = csv.reader(csv_file)

    # Skip the rows before the start index
    for _ in range(start_index):
        next(reader)

    # Iterate over the rows and check if any row matches the search query
    for i, row in enumerate(reader):
        row_hash = [hashlib.sha256(value.encode()).hexdigest() for value in row]
        for query_row in rows_to_search:
            if row_hash == query_row:
                print(f"Process {rank} found row: {row}")

        # Break the loop if we have reached the end index
        if i == end_index - 1:
            break
