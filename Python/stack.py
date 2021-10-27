#!/usr/bin/env python3

# A Basic Stack - v1, 10/27/2021

"""
PUSH - Pushes a new item to the top of the stack
POP - Removes the top item of the stack
PEEK - Returns the stack pointer location (should always be the top item)
DUPL - Duplicates the top item and puts it to the top of the stack
SWAP - Swaps the positions of the top two items on the stack
OVER - Duplicates the item 2nd from the top and puts it to the top of the stack
STACK - Shows the current state of the stack
EXIT - Exits the program
"""

stack = []

while True:
    command = input()

    if command.upper() == "PUSH":
        try:
            stack.append(stack[-1]+1)
        except IndexError:
            stack.append(1)
        print("Pushed to stack successfully.")
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
    if command.upper() == "STACK":
        if stack != []:
            stack.reverse()
            print("-")
            for i in stack:
                print(i)
            stack.reverse()
            print("-")
            print("")
        else:
            print("The stack is empty.")
            print("")
    if command.upper() == "EXIT":
        exit()

    else:
        print("")
