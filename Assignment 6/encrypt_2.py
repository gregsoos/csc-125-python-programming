# -*- coding: utf-8 -*-
"""
Program: encrypt_2.py
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

# Apply Caesar cipher to message (no wrap-around case)
code = ""
for ch in text:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    code += chr(cipherValue)

# Write output to new file
outputFile = open(outputName, 'w')
outputFile.write(code)
outputFile.close()