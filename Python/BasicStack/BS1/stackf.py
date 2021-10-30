#!/usr/bin/env python3

# Basic Stack (BS1) - 10/30/2021
# An (unofficial) variant of "Super Stack!"
# Learn about it here: https://esolangs.org/wiki/Super_Stack!
# Turing-completeness is unknown

# Reference Implementation - File Interpreter
# Recommended Python version: 3.6+ 

# Order: Last in, first out
# ASCII commands display the stack in the opposite order

# Scripts must be written in lowercase.
# One instruction per line.

# David Costell - davidcostell44@gmail.com

if __name__ != "__main__": # Standard boilerplate
    exit()

stack = [] # The stack is initialized here.

def split(text: str) -> (str, str): # Function that enables args
    text = text.strip()
    space = text.find(' ')
    if space > 0:
        return text[:space], text[space + 1:]
    return text, ""

def showstack(x): # Function showing the stack
    x.reverse()
    print("-")
    for i in x:
        print(i)
    x.reverse()
    print("-")

print("Basic Stack Interpreter",
      "Enter a filename (e.g. myscript.txt) to begin.",
      "", sep="\n")

while True:
    in_put = input("")
    if in_put.lower() == "exit":
        exit()

    # Interpreter Begin

    stack = [] # Wipe the stack before execution.
    # This will make sure no artifacts are left behind
    # from any previous scripts run by the interpreter.
    print("",
          "Execution Begin",
          "-------------------------------------",
          "",
          sep="\n")
    try:
        file = open(in_put)
    except FileNotFoundError:
        file = "Placeholder to prevent being undefined"
        print("The file was not found.",
              "Check that you have spelled the filename correctly,",
              "and that it exists in the system.",
              "",
              sep="\n")
        input()
        exit(1)

    lines = file.readlines()
    for line in lines: # Iterate over the input file's lines
            
        line, args = split(line) # Allows arguments to be used in input file

        # Check if line is a comment, and if it is, ignore any instruction in it
        if line.startswith("#"):
            pass

        # Core Operations

        if line == "push": # Push a value higher than the last value
            try:
                stack.append(int(stack[-1])+1)
            except IndexError:
                stack.append(1)
            print("Pushed to stack successfully.")
        if line == "pushv": # Push a specified value
            if args != "":
                try:
                    if int(args) > -1:
                        stack.append(int(args))
                        print("Pushed specified val to stack successfully.")
                    else:
                        print("Cannot push a negative number.")
                except ValueError:
                    print("Invalid specified value.")
            else:
                print("No value specified.")
        if line == "pushr": # Push a specified number of times
            if args != "":
                try:
                    for _ in range(int(args)):
                        try:
                            stack.append(int(stack[-1])+1)
                        except IndexError:
                            stack.append(1)
                    print("Pushed the specified number of times to stack successfully.")
                except ValueError:
                    print("Invalid specified value.")
            else:
                print("No value specified.")

        if line == "pop": # Pop the last value
            if stack != []:
                stack.pop()
                print("Popped successfully.")
            else:
                print("The stack is empty.")
        if line == "popr": # Pop a specified number of times
            if args != "":
                try:
                    for _ in range(int(args)):
                        stack.pop()
                except IndexError:
                    print("Value exceeded number of values in the stack! Stack emptied.")
                except ValueError:
                    print("Invalid specified value.")
                print("Popped the specified number of times successfully.")
            else:
                print("No value specified.")

        # Advanced Operations

        if line == "peek": # Shows the stack's last value (stack pointer)
            try:
                print("Stack pointer:", stack[-1])
            except IndexError:
                print("The stack is empty.")
        if line == "dupl": # Duplicates the last value and pushes it to the stack
            if stack != []:
                stack.append(stack[-1])
                print("Duplication complete.")
            else:
                print("Nothing to duplicate.")
        if line == "swap": # Swap the positions of the top two values
            if stack != []:
                stack.reverse()
                a = stack[0]
                stack[0] = stack[1]
                stack[1] = a
                stack.reverse()
                print("Swap complete.")
            else:
                print("Nothing to swap.")
        if line == "over": # Duplicate the second last value to the top of the stack
            if stack != []:
                stack.append(stack[-2])
                print("Over operation complete.")
            else:
                print("Nothing to put over the stack.")

        if line == "rot": # Rotate the stack clockwise
            if stack != []:
                stack = [stack[(i + 3) % len(stack)] for i, x in enumerate(stack)]
                print("Rotated the stack clockwise.")
            else:
                print("Nothing to rotate in the stack.")
        if line == "rotcc": # Rotate the stack counterclockwise
            if stack != []:
                stack = [stack[(i - 3) % len(stack)] for i, x in enumerate(stack)]
                print("Rotated the stack clockwise.")
            else:
                print("Nothing to rotate in the stack.")

        # The following two commands functionally perform the same action:
        # They swap the positions of the top and bottom values.
        # However, they are split into two to represent "CYCLE" and "RCYCLE" equivalents.
        if line == "top":
            if stack != []:
                stack[0], stack[-1] = stack[-1], stack[0]
                print("Top value swapped to the bottom of the stack.")
            else:
                print("Nothing to swap the top to the bottom of the stack.")
        if line == "bot":
            if stack != []:
                stack[-1], stack[0] = stack[0], stack[-1]
                print("Bottom value swapped to the top of the stack.")
            else:
                print("Nothing to swap to the bottom of the top of the stack.")

        if line == "rev": # Reverse the stack
            stack.reverse()
            print("Stack reversed.")


        # Mathematical Operations

        if line == "add":
            if stack != []:
                a1 = stack[-1]
                a2 = stack[-2]
                for i in range(2):
                    stack.pop()
                a3 = a1 + a2
                print("Sum:", a3)
                stack.append(a3)
            else:
                print("The stack is empty.")
        if line == "sub":
            if stack != []:
                a1 = stack[-1]
                a2 = stack[-2]
                for i in range(2):
                    stack.pop()
                a3 = a1 + a2
                print("Difference:", a3)
                stack.append(a3)
            else:
                print("The stack is empty.")
        if line == "mul":
            if stack != []:
                a1 = stack[-1]
                a2 = stack[-2]
                for i in range(2):
                    stack.pop()
                a3 = a1 + a2
                print("Product:", a3)
                stack.append(a3)
            else:
                print("The stack is empty.")
        if line == "div":
            if stack != []:
                a1 = stack[-1]
                a2 = stack[-2]
                for i in range(2):
                    stack.pop()
                a3 = a1 + a2
                print("Quotient:", a3)
                stack.append(a3)
            else:
                print("The stack is empty.")
        if line == "mod":
            if stack != []:
                a1 = stack[-1]
                a2 = stack[-2]
                for i in range(2):
                    stack.pop()
                a3 = a1 % a2
                print("Modulo:", a3)
                stack.append(a3)
            else:
                print("The stack is empty.")

        # ASCII Operations

        if line == "ascii": # Convert all stack values to corresponding ASCII character
            if stack != []:
                try:
                    asclist = []
                    for i in stack:
                        asc = chr(int(i))
                        print(i, asc)
                        asclist.append(asc)
                    ascstr = ""
                    ascstr = ascstr.join(asclist)
                    print("String form:", ascstr)
                except OverflowError:
                    print("One of the stack's values are too large.")
                except ValueError:
                    print("ValueError while attempting ASCII conversion.")
            else:
                print("The stack is empty.")
        if line == "conv": # Converts specified string to ASCII (does not push)
            conv = args # This instruction is useless in the context of this interpreter,
            values = [] # however it has been preserved here for 100% specification compliance.
            for character in conv:
                values.append(ord(character))
            print("Converted string to ASCII:")
            print(values)
        if line == "convp": # Converts specified string to ASCII and pushes them as values
            conv = args
            values = []
            for character in conv:
                values.append(ord(character))
            stack.extend(values)
            print("Converted string to ASCII and pushed to stack:")
            print(values)

        # Other Operations

        if line == "wipe": # Wipe the stack of values
            stack = []
            print("Stack wiped.")
        if line == "stack": # Shows the stack
            if stack != []:
                showstack(stack)
            else:
                print("The stack is empty.")

    file.close()
    print("",
          "-------------------------------------",
          "Execution End",
          "",
          "Enter another filename or enter EXIT to exit.",
          "",
          sep="\n")
    # Interpreter End
