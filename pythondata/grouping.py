# Filtering exercise from the last date of class
import csv
import json
from pprint import pprint


with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = [dict(row) for row in reader] # Convert Ordered Dict to regular dict (python 3.6 or higher)

vegetables = str(rows)
#Read vegtables.csv into a variable called vegtables.
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
pprint(vegetables)

vegetables_by_color = {}
for veg in vegetables:
	color = veg["color"]
	if veg in vegetables_by_color:
		vegetables_by_color[veg]+=1
	else:
		vegetables_by_color[veg] = 1
pprint(vegetables_by_color)


# source consulted - https://stackoverflow.com/questions/35558053/load-csv-file-into-list