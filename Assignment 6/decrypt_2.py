# -*- coding: utf-8 -*-
"""
Program: decrypt_2.py
Author: Greg Soos
Last date modified: 04.04.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: Modify the scripts of Projects 1 and 2 to encrypt and decrypt entire files of text
"""

# Take the inputs
inputName = input("Enter the name of the input file: ")
outputName = input('Enter the name of the output file: ')
distance = int(input('Enter the distance: '))

# Open file
inputFile = open(inputName, 'r')
text = inputFile.read()

# Decrypt message using Caesar cipher (no wrap-around cases)
plainText = ""
for ch in text:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue > 0: # Prevent attempting to append characters outside range of chr function
        plainText += chr(cipherValue) 

# Write output to new file
outputFile = open(outputName, 'w')
outputFile.write(plainText)
outputFile.close()

# This is to prevent duplication