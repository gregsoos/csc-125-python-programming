"""
Program: copyfile.py
Author: Greg Soos
Last date modified: 04.11.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: Write a script named copyfile.py. This script should prompt the user for the
names of two text files. The contents of the first file should be input and written
to the second file.
"""

# Take the inputs
fileNameIn = input("Enter the name of the first file: ")
fileNameOut = input("Enter the name of the second file: ")

# Open both files
inputFile = open(fileNameIn, 'r')
outputFile = open(fileNameOut, 'w')

# Copy text from first file to second file
text = inputFile.read()
outputFile.write(text)
outputFile.close()