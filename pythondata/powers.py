# Authors: Dima and Sarah
# This should be run in python3 (not 2) to avoid the appearance of unicode symbols

# Read superheroes.json
import json

with open('superheroes.json', 'r') as f:
    squad = csv.load(f) 
    
# To test functionality, take "print(squad)" out of the comments and run powers.py in ubuntu

# Create empty array called powers
allpowers = []

# First we need a list of members
members = squad['members']  # For this entire dictionary of squad, this accesses the key members

# Loop through the members of the squad and append the powers of each member to the powers array.
for member in members:
	powers = member['powers']
	for power in powers:
		allpowers.append(power)

# Print each power to the terminal.
print(allpowers)