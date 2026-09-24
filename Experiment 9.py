import csv
import json

# File names
input_file = "input.csv"
output_file = "output.json"

# Read data from CSV file
with open(input_file, "r") as csv_file:
    csv_data = csv.DictReader(csv_file)

    # Convert CSV data into a list
    data = list(csv_data)

# Write data to JSON file
with open(output_file, "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV file successfully converted to JSON.")
print(f"JSON data saved to: {output_file}")
