import csv
import random

# Generate CSV file with 1,000,000 records
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Generate 1,000,000 records
    for _ in range(1000000):

        # Generate 20 random int32 values between 0 and 100
        record = [random.randint(0, 100) for _ in range(20)] 
        writer.writerow(record)
