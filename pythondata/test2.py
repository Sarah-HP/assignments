import json

rows = [
    {"name": "Rachel", "age": 34}, #Each item in the list is a person
    {"name": "Monica", "age": 34},
    {"name": "Phoebe", "age": 37}
]

with open('friends.json', 'w') as f: #This is a context manager. We are naming our variable "f"
    json.dump(rows, f, indent=2) # json.dump takes in 1) the data, and 2) the file where we want to dump the data
	# note that this created a new file in the same folder called friends.json

# Now to have a snippet of code that opens a json file (remove comments, indents, and preceding code to run)
	#import json

	#with open('friends.json', 'r') as f:
	#    data = json.load(f)
	    
	#print(data)