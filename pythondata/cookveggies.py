# Take a csv and end up with a json format

# Read vegetables.csv file
import csv

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = [dict(row) for row in reader] # Convert Ordered Dict to regular dict (python 3.6 or higher)

print(vegetables)

# Conversion (??)

# Write json file called vegetables.json
import json

with open('vegetables.json', 'w') as f:
    json.dump(vegetables, f)