import csv
import logging
# Step 1: Setup logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Step 2: take input from user

filename = input("Enter input CSV file name (e.g., Week1/data.csv): ")
output_file = input("Enter output CSV file name (e.g., Week1/adults.csv): ")
# Step 3: Process the csv

try:
    with open(filename, mode='r') as file, open(output_file, mode='w', newline='') as output:
        reader = csv.DictReader(file)
        fieldnames = ['name', 'age', 'city']
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
        # Step 4: Filter rows where age >= 18
        
            if row['age'] and int(row['age']) >= 18:
                writer.writerow(row)
                logging.info(f"Saved: {row['name']} (age {row['age']})")
except FileNotFoundError:
    logging.error("File not found. Please check the filename.")
except Exception as e:
    logging.error(f"Something went wrong: {e}")