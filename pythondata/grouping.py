# Filtering exercise from the last date of class
import csv
import json
from pprint import pprint


# with open('vegetables.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     rows = [dict(row) for row in reader] # Convert Ordered Dict to regular dict (python 3.6 or higher)
# # pprint(f)
# # vegetables = list(rows)

# #Read vegtables.csv into a variable called vegtables.
	# Blocked here - I've tried a number of variations of code (some of which are shown below), but with no success
		# # Read vegetables.csv into a variable called vegetables.
		# import csv
		# with open('vegetables.csv', 'wb') as csvfile:
		#     vegetables = csv.writer(csvfile)
		#     # Trying code from - https://docs.python.org/2/library/csv.html#examples

		# vegetables=[]
		# with open('vegetables.csv', 'r') as f:
		#    reader = csv.DictReader(f)
		#    rows = [dict(row) for row in reader] 
		#    for row in reader:
		#    	line
		#    vegetables = list(reader)
		# pprint(vegetables)
		# # print(rows)
# I was struggling with the CSV, so I'm just going to bring in the dataframe

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

# Make an empty dictionary
vegetables_by_color = {}
# loop through the "vegetables" list of dictionaries
for veg in vegetables:
	color = veg['color']
	if color in vegetables_by_color:
		vegetables_by_color[color].append(veg)
	else:
		vegetables_by_color[color] = [veg]
#Print things out
pprint(vegetables_by_color)


# Output vegetables_by_color into a json
with open('vegetables_by_color.json', 'w') as f:
    json.dump(vegetables_by_color, f)


# # source consulted - https://stackoverflow.com/questions/35558053/load-csv-file-into-list, http://sthurlow.com/python/lesson06/