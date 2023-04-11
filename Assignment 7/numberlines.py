"""
Program: numberlines.py
Author: Greg Soos
Last date modified: 04.11.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: Write a script named numberlines.py. This script creates a program listing from a
source program. This script should prompt the user for the names of two files. The
input filename could be the name of the script itself, but be careful to use a different
output filename! The script copies the lines of text from the input file to the output
file, numbering each line as it goes. The line numbers should be right-justified in
4 columns, so that the format of a line in the output file looks like this example:
   1> This is the first line of text.
"""

# Take the inputs
fileNameIn = input("Enter the name of a file to line-number: ")
fileNameOut = input("Enter the name of a file to output to: ")

# Open both files
inputFile = open(fileNameIn, 'r')
outputFile = open(fileNameOut, 'w')

# Number lines and write to output file
i = 1
while True:
    line = inputFile.readline()
    if line == "":
        break
    outputFile.write('%4s' % i + '> ' + line)
    i += 1

# Close output file
outputFile.close()