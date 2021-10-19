#!/usr/bin/env python3

# Collatz Conjecture
# Python 3.5+

# David Costell - 10/19/2021

import math

number = input('Enter a number: ')
try:
    number = float(number)
except:
    print('Error: Could not convert to integer.')
    print('Only integers/floats can be entered as input.')
    input()
    exit()

if number == 0:
    input('Error: Zero is not calculable. ')
    exit()
if number < 0:
    input('Error: Negative numbers are not calculable. ')
    exit()
if number == math.inf:
    input('Error: Infinity is not calculable.')
    exit()

print('Number is', number)
input('Press ENTER to begin.')
print('BEGIN COLLATZ SEQUENCE')

def modulo():
    global number
    modulo = number % 2
    if modulo == 0:
        number = number / 2
    else:
        number = number * 3 + 1
    
def printnum(x):
    print(x)

def final():
    print('END COLLATZ SEQUENCE')
    print('Program has reached a 4-2-1 loop.')
    input()
    exit()
    
while True:      
    modulo()
    printnum(number)
    if number == 1.0:
        break

final()
