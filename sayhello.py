#!/usr/bin/env python3
import sys
# Taking standard input and saving it in a variable called "name"
# This is a python program that should say the person's name when prompted
name = sys.stdin.read()
print("Hello " + name + "!")

# If I run: "chmod +x sayhello.py" the program becomes executable
# I can then pipe in info. e.g. echo -n "my name" | ./sayhello.py