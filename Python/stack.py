#!/usr/bin/env python3

# Basic Stack - v3, 10/28/2021

# Order: Last in, first out
# ASCII command displays stack values in the opposite order

"""
PUSH - Pushes a new item to the top of the stack
PUSHV [number] - Pushes a specific value to the top of the stack
    The number argument has to be a valid decimal integer.
POP - Removes the top item of the stack
STACK - Shows the current state of the stack

PEEK - Returns the top value of the stack
DUPL - Duplicates the top item and puts it to the top of the stack
SWAP - Swaps the positions of the top two items on the stack
OVER - Duplicates the item 2nd from the top and puts it to the top of the stack
WIPE - Empties the stack of any values (irreversible)

ASCII - Converts stack values to corresponding ASCII characters
    65-90 (40-5A) - [A-Z] uppercase letters
    97-122 (61-7A) - [a-z] lowercase letters
CONV [string] - Converts string's characters to corresponding ASCII chars
CONVP [string] - Same as CONV, but pushes the values to the stack.

EXIT - Exits the program

PUSHV means Push val
CONVP means Convert push
"""

stack = []

def split(text: str) -> (str, str):
    text = text.strip()
    space = text.find(' ')
    if space > 0:
        return text[:space], text[space + 1:]
    return text, ""

print("Basic Stack v3")
print("")

while True:
    command = input()
    command, args = split(command)

    if command.upper() == "PUSH":
        try:
            stack.append(int(stack[-1])+1)
        except IndexError:
            stack.append(1)
        print("Pushed to stack successfully.")
    if command.upper() == "PUSHV":
        if args != "":  
            try:
                stack.append(args)
                print("Pushed specified val to stack successfully.")
            except ValueError:
                print("Invalid specified value.")
        else:
            print("No value specified.")
            
    if command.upper() == "POP":
        if stack != []:
            stack.pop() 
            print("Popped successfully.")
        else:
            print("The stack is empty.")


    if command.upper() == "PEEK":
        try:  
            print("Stack pointer:", stack[-1])
        except IndexError:
            print("The stack is empty.")
    if command.upper() == "DUPL":
        if stack != []:
            stack.append(stack[-1])
            print("Duplication complete.")
        else:
            print("Nothing to duplicate.")
    if command.upper() == "SWAP":
        if stack != []:
            stack.reverse()
            a = stack[0]
            stack[0] = stack[1]
            stack[1] = a
            stack.reverse()
            print("Swap complete.")
        else:
            print("Nothing to swap.")
    if command.upper() == "OVER":
        if stack != []:
            stack.append(stack[-2])
            print("Over operation complete.")
        else:
            print("Nothing to put over the stack.")

            
    if command.upper() == "ASCII":
        if stack != []:
            try:
                asclist = []
                for i in stack:
                    asc = chr(int(i))
                    print(i, asc)
                    asclist.append(asc)
                ascstr = ""
                ascstr = ascstr.join(asclist)
                print("String:", ascstr)
            except OverflowError:
                print("One of the stack's values are too large.")
            except ValueError:
                print("ValueError while attempting ASCII conversion.")
        else:
            print("The stack is empty.")
    if command.upper() == "CONV":
        conv = args
        values = []
        for character in conv:
            values.append(ord(character))
        print("Converted string to ASCII:")
        print(values)
    if command.upper() == "CONVP":
        conv = args
        values = []
        for character in conv:
            values.append(ord(character))
        stack.extend(values)
        print("Converted string to ASCII and pushed to stack:")
        print(values)

    if command.upper() == "WIPE":
        stack = []
        print("Stack wiped.")
    if command.upper() == "STACK":
        if stack != []:
            stack.reverse()
            print("-")
            for i in stack:
                print(i)
            stack.reverse()
            print("-")
        else:
            print("The stack is empty.")
    if command.upper() == "EXIT":
        exit()

    else:
        print("")
