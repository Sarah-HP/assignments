# Reads name.txt into a variable my_name

with open('name.txt') as f:
	my_name = f.read()

# Construct greeting (the "\n" just starts a new line)
greeting = 'Helo my name is ' + my_name + "." + '\n'
print(greeting)

# Write that to a file
with open('hello.txt', 'w') as f:
	f.write(greeting)

# Remember: we read from one format, do something in the middle to modify, and then output to a different file