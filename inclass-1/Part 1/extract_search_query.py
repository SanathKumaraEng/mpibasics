import csv

# Open the CSV file
with open('data.csv', 'r') as csv_file:
    # Create a CSV reader object
    reader = csv.reader(csv_file)
    
    # Initialize a list to store the selected rows
    selected_rows = []
    
    # Define the indices to extract
    indices = [0, 10, 20, 50, 100000, 500000]
    
    # Iterate over the rows and check if the index matches
    for i, row in enumerate(reader):
        if i in indices:
            selected_rows.append(row)

# Create the search query file
with open('search_queries.txt', 'w') as file:
    # Iterate over the selected rows
    for row in selected_rows:
        # Write each row to the file, separating values by commas
        file.write(','.join(row) + '\n')