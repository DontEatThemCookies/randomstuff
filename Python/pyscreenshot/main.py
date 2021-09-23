#!/usr/bin/env python3
# Above line is for Linux clients

# Python program to take screenshots - v1 9-23-2021
# Dependencies: numpy, opencv-python, pyautogui, pillow (not PIL)
# python3 -m pip install [dependency]
# Substitute "python3" to "py" or "python.exe" if it fails to execute.

# Programmed in Python for Windows

##################################################
#               PYTHON DEPENDENCIES
import numpy as np
import cv2
import pyautogui
#
##################################################
#             BUILT-IN PYTHON MODULES
import os
import uuid 
import ctypes
import subprocess

from tkinter import *
from os import system, name
from time import sleep
#
##################################################

scriptname = os.path.basename(__file__)
init = "Initialized! Script name: "
alt = "Python Screenshot [MacOS/Linux/POSIX]"

def title():

    if name == 'nt':
        _ = ctypes.windll.kernel32.SetConsoleTitleW("Python Screenshot [Windows]")
    else:
        _ = print(f'\33]0;{alt}\a', end='', flush=True)

def quit(event):
    exit() # Tkinter code, to be used in future versions

title()

# Initialization

A = 1

if A > 1:
    print("Screenshot taken!")

print(init+scriptname)
print("")
print("Python Screenshot - Fullscreen screenshots")
print("")
print("This script should be run directly and not from the command line.")
print("This program will return to this screen automatically after each screenshot.")
print("Image will be named randomly and saved to the folder containing this script.")
print("")
input("Press ENTER once ready to take the screenshot. Otherwise, CTRL + C to exit.")

filename = str(uuid.uuid4()) # Define filename as a random UUID
string2 = ".png" # Define the image format to be saved - changeable to JPG/JPEG
name = filename+string2 # Concantenate the two strings to be used by CV2.

# Take the screenshot using pyautogui
image = pyautogui.screenshot()
   
# Convert to numpy array so it can be written to the disk.
image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
   
# Saves the image.
cv2.imwrite(name, image)

print("")
with open('main.py') as infile:
    exec(infile.read())
# exec(open('main.py').read())
# old method of opening file

# EOF
