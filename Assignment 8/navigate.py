"""
Program: navigate.py
Author: Greg Soos
Last date modified: 04.18.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: Write a program that allows the user to navigate the lines of text in a file. The
program should prompt the user for a filename and input the lines of text into a
list. The program then enters a loop in which it prints the number of lines in the
file and prompts the user for a line number. Actual line numbers range from 1 to
the number of lines in the file. If the input is 0, the program quits. Otherwise, the
program prints the line associated with that number.
"""

# Request file to read and open
fileName = input("Enter the filename: ")
myFile = open(fileName, 'r')

# Create list of each line of text in file
text = []
while True:
    line = myFile.readline()
    if line == "":
        break
    text.append(line[:-1]) # Exclude newline characters

# Display total number of lines, prompt user for line to print    
print(f'The number of lines in the file is {len(text)}.')
while True:
    lineNumber = int(input('Enter a line number: '))
    if lineNumber == 0:
        break
    print(f'{text[lineNumber - 1]}\n')
