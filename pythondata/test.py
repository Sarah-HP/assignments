#mydict= {
#	'a':1,
#	'b':2,
#	'c': 3
#}

#print(mydict['b'])


## Try printing my list. These things will show up if Ijust type "python3 test.py" into my command terminal (when I'm in the right directory)
#mylist = [1, 2, 3]
#print(mylist[0])

#mylist.append(4)
#print(mylist)


## grab thelast element
#print(mylist[-1])


## Now work on opening files
# the first argument is the name of the file; the second is either the letter w, r, or a

#with open('testwrite.txt', 'w') as f:

# Read name.txt
with open('name.txt') as f:
	my_name = f.read()
print(my_name)

# Create greeting
greeting = "Hello, my name is " + my_name + "."
print(greeting)

# Write hello.txt 
with open('greeting.txt', 'w') as f:
	f.write(greeting)
	f.write('\n')
