#!/usr/bin/env python3

# Basic Stack (BS1) - 10/29/2021
# An (unofficial) variant of "Super Stack!"
# Learn about it here: https://esolangs.org/wiki/Super_Stack!
# Turing-completeness is unknown

# Reference Implementation
# Recommended Python version: 3.6+ 

# Order: Last in, first out
# ASCII commands display the stack in the opposite order

# David Costell - davidcostell44@gmail.com

"""

Instructions

PUSH - Pushes a new item to the top of the stack
PUSHV [number] - Pushes a specific value to the top of the stack
    The number argument has to be a valid decimal integer.
PUSHR [number] - Pushes a specific number of times to the top of the stack
    The number argument has to be a valid decimal integer.
    If the number argument defined is large (>8 numbers), it may take a long time
POP - Removes the top item of the stack
POPR [number] - Pops values from the stack a specific number of times
    The number argument has to be a valid decimal integer.
    If the argument exceeds the number of actual values in the stack,
    it will be emptied.
    
STACK - Shows the stack (LI-FO order)

PEEK - Returns the top value of the stack
DUPL - Duplicates the top item and puts it to the top of the stack
SWAP - Swaps the positions of the top two items on the stack
OVER - Duplicates the item 2nd from the top and puts it to the top of the stack
ROT - Rotates top three values of the stack clockwise
ROTCC - Rotates top three values of the stack counterclockwise

TOP - Top value of the stack is placed in the bottom
BOT - Bottom value of the stack is placed in the top
REV - Reverses entire stack

TOP and BOT practically do the same thing.
This was split into two commands to be parallel with "CYCLE" and "RCYCLE"

WIPE - Empties the stack (irreversible)

ADD - Pops top two values, adds them and pushes the result
SUB - Pops top two values, subtracts them and pushes the result
MUL - Pops top two values, multiplies them and pushes the result
DIV - Pops top two values, divides them and pushes the result
MOD - Pops top two values, does modulus on them and pushes the result

ASCII - Converts stack values to corresponding ASCII characters
    Similar to INPUTASCII
    10 (0A) - Line Feed (newline)
    65-90 (40-5A) - [A-Z] uppercase letters
    97-122 (61-7A) - [a-z] lowercase letters
CONV [string] - Converts string's characters to corresponding ASCII chars
    Follow the order of ASCII numbers outputted here if you plan
    to manually PUSHV the ASCII values into the stack.
CONVP [string] - Same as CONV, but pushes the values to the stack
    Similar to OUTPUTASCII

EXIT - Exits the program

PUSHV means Push value
PUSHR means Push repeat
POPR means Pop repeat
CONVP means Convert push

To Be Implemented:

LOOP - Enters loop mode. The next command issued will be looped.
    Similar to "IF" in Super Stack!
END - Ends any loop.
    Similar to "FI" in Super Stack!

"""

stack = [] # The stack is initialized here.

def split(text: str) -> (str, str):
    text = text.strip()
    space = text.find(' ')
    if space > 0:
        return text[:space], text[space + 1:]
    return text, ""

def showstack(x):
    x.reverse()
    print("-")
    for i in x:
        print(i)
    x.reverse()
    print("-")

def asc(x, y):
    asclist = []
    for i in stack:
        asc = chr(int(i))
        if y != 0: 
            print(i, asc)
        asclist.append(asc)
    ascstr = ""
    ascstr = ascstr.join(asclist)
    print("String:", ascstr)

print("Basic Stack",
      "Input commands",
      "",
      sep="\n")

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
                if int(args) > -1:
                    stack.append(int(args))
                    print("Pushed specified val to stack successfully.")
                else:
                    print("Cannot push a negative number.")
            except ValueError:
                print("Invalid specified value.")
        else:
            print("No value specified.")
    if command.upper() == "PUSHR":
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
        
            
    if command.upper() == "POP":
        if stack != []:
            stack.pop() 
            print("Popped successfully.")
        else:
            print("The stack is empty.")
    if command.upper() == "POPR":
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
            
    if command.upper() == "ROT":
        if stack != []:
            stack = [stack[(i + 3) % len(stack)] for i, x in enumerate(stack)]
            print("Rotated the stack clockwise.")
            #showstack(stack) Uncomment for convenience in debugging
        else:
            print("Nothing to rotate in the stack.")
    if command.upper() == "ROTCC":
        if stack != []:
            stack = [stack[(i - 3) % len(stack)] for i, x in enumerate(stack)]
            print("Rotated the stack counter-clockwise.")
            #showstack(stack) Uncomment for convenience in debugging
        else:
            print("Nothing to rotate in the stack.")

    if command.upper() == "TOP":
        if stack != []:
            stack[0], stack[-1] = stack[-1], stack[0]
            print("Top value swapped to the bottom of the stack.")
        else:
            print("Nothing to swap the top to the bottom of the stack.")
    if command.upper() == "BOT":
        if stack != []:
            stack[-1], stack[0] = stack[0], stack[-1]
            print("Bottom value swapped to the top of the stack.")
        else:
            print("Nothing to swap the bottom to the top of the stack.")

    if command.upper() == "REV":
        stack.reverse()
        print("Stack reversed.")
        

    if command.upper() == "ADD":
        if stack != []:
            a1 = stack[-1]
            a2 = stack[-2]
            for i in range(2):
                stack.pop()
            a3 = a1+a2
            print("Sum:", a3)
            stack.append(a3)
        else:
            print("The stack is empty.")
    if command.upper() == "SUB":
        if stack != []:
            a1 = stack[-1]
            a2 = stack[-2]
            for i in range(2):
                stack.pop()
            a3 = a1-a2
            print("Difference:", a3)
            stack.append(a3)
        else:
            print("The stack is empty.")
    if command.upper() == "MUL":
        if stack != []:
            a1 = stack[-1]
            a2 = stack[-2]
            for i in range(2):
                stack.pop()
            a3 = a1*a2
            print("Product:", a3)
            stack.append(a3)
        else:
            print("The stack is empty.")
    if command.upper() == "DIV":
        if stack != []:
            a1 = stack[-1]
            a2 = stack[-2]
            for i in range(2):
                stack.pop()
            a3 = a1-a2
            print("Quotient:", a3)
            stack.append(a3)
        else:
            print("The stack is empty.")
    if command.upper() == "MOD":
        if stack != []:
            a1 = stack[-1]
            a2 = stack[-2]
            for i in range(2):
                stack.pop()
            a3 = a1%a2
            print("Modulo:", a3)
            stack.append(a3)
        else:
            print("The stack is empty.")
        
                    
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
                print("String form:", ascstr)
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
            showstack(stack)
        else:
            print("The stack is empty.")
    if command.upper() == "EXIT":
        exit()

    else:
        print("")
