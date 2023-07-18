import csv
import random
import string

def generate_random_string(length):
    """Generate a random string of given length"""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# Generate CSV file with 1,000,000 records
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Generate 1,000,000 records
    for _ in range(1000000):
        # Generate 20 random strings with length <= 10
        record = [generate_random_string(random.randint(1, 10)) for _ in range(20)] 
        writer.writerow(record)