"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    calculation = raw_input("> ")
    tokens = calculation.split(" ")
    if tokens[0] == "q":
        print "You will exit."
        break
    else:
        if tokens[0] == "+" and len(tokens) == 3:
            print add(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == "-" and len(tokens) == 3:
            print subtract(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == "*" and len(tokens) == 3:
            print multiply(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == "/" and len(tokens) == 3:
            print divide(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == "square" and len(tokens) == 2:
            print square(int(tokens[1]))
        elif tokens[0] == "cube" and len(tokens) == 2:
            print cube(int(tokens[1]))
        elif tokens[0] == "pow" and len(tokens) == 3:
            print power(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == "mod" and len(tokens) == 3:
            print mod(int(tokens[1]), int(tokens[2]))
        else:
            print "Invalid arguments. Try again or enter q to quit."
