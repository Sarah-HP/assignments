#import csv

#with open('testwrite.csv', 'w') as f:																

 #   writer = csv.writer(f)

    # Write Header
  #  writer.writerow(['col1', 'col2'])

    # Write Data -- note: This requires a list, but we can input the list with numeric data instead
    # If we use double quotes instead of single quotes, the quotes themselves will show up in the .csv with an escape character
  #  writer.writerow(['val1', 'val2'])
  #  writer.writerow(['val1', 'val2'])
  #  writer.writerow(['val1', 'val2'])


# Now open up the file
	import csv

	with open('testwrite.csv', 'r') as f:
	    reader = csv.DictReader(f) #DictReader reads into a list of dictionaries
	    rows = [dict(row) for row in reader] # Convert Ordered Dict to regular dict (python 3.6 or higher)

	print(rows)

# Note: if you load in "pandas", you can treat the data like a dataframe and manipulate accordingly


# csv.reader takes an item that is iterable
# key / value pairs: {Key: Value} (we have "key 1, value 1," "key 2, value 2", etc. in our dict.reader)

