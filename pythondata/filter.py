# Filtering exercise from the last date of class
import csv
import json

# Read vegetables.csv into a variable called vegetables.
with open('vegetables.csv', 'r') as f:
   reader = csv.DictReader(f)
   rows = [dict(row) for row in reader] # Convert Ordered Dict to regular dict (python 3.6 or higher)
# print(rows)

# Loop through vegetables and filter down to only green vegtables using a whitelist.
green_vegetables = []
whitelist = ['broccoli', 'okra', 'arugula']
for row in rows:
    if row['name'] in whitelist:
        green_vegetables.append(row)

# Print veggies to the terminal
print(green_vegetables)

# Write the veggies to a json file called greenveggies.json
with open('greenveggies.json', 'w') as outfile:
    json.dump(green_vegetables, outfile)

# Bonus: Output to csv
with open('greenveggies.csv', 'w') as f:
    writer = csv.writer(f)
    # Write the top row
    writer.writerow(['name', 'color'])
    # loop through & write 1 row per veggie
    for gveggie in green_vegetables:
    	name = gveggie['name']
    	color = gveggie['color']
    	writer.writerow([name, color])

########################################Alternative Code########################

# Sarah and Dima

# Read vegetables.csv into a variable called vegetables.

# import csv
# from pprint import pprint
# import json

# with open(‘vegetables.csv’, ‘r’) as f:
#    reader = csv.DictReader(f)
#    vegetables = [dict(row) for row in reader] # Try with and without -- Convert Ordered Dict to regular dict (python 3.6 or higher)

# # Loop through vegetables and filter down to only green vegtables using a whitelist.

# green_vegetables = []
# whitelist = [‘green’]
# for veggie in vegetables:
#    if veggie[‘color’] in whitelist:
#        green_vegetables.append(veggie)

# # Print veggies to the terminal
# print(green_vegetables)

# # Write the veggies to a json file called greenveggies.json


# with open(‘greenveggies.json’, ‘w’) as f:
#    json.dump(green_vegetables, f, indent=2)


# # Bonus: Output another csv called green_vegetables.csv.