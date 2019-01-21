import csv # This is a python package (AKA library) telling python that we want to work with csv
			# It is best practice to import the library at the top

# Add some data
# "vegetables" is a list (a bunch of things in an orders) made up of dictionaries
vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

# Double check that the code works
print(vegetables)

# Now loop through each vegetable
for veggie in vegetables:
	print(veggie)

# Write the vegetable as a CSV

with open('vegetables.csv', 'w') as f: # f is just a variable. We could call it anything
    writer = csv.writer(f)
    writer.writerow(['name', 'color', 'length_of_name']) # This writes teh first row in the data (the header)
    # Write data

    # Loop through each vegetable
    for veggie in vegetables:
    	veggiename = veggie['name'] #This accesses the value
    	color = veggie['color']
    	for letter in veggiename:
    		length_of_name=len(veggiename) # This is the bonus
    	writer.writerow([veggiename, color, length_of_name]) # Now we are telling python to write a row in our csv