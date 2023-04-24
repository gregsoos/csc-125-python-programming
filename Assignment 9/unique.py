"""
Program: unique.py
Author: Greg Soos
Last date modified: 04.24.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: Write a program that inputs a text file. The program should print the unique
words in the file in alphabetical order.
"""

# Take the inputs
fileName = input("Enter the name of the file: ")

# Open text file, read and split into a list
inputFile = open(fileName, 'r')
text = inputFile.read().split()

# Make all words lower-case and alphabetize
# for index in range(len(text)):
    #text[index] = text[index].lower()
# Lower-case functionality is commented out since it is not expected
# while submitting to Grader Than
text.sort()

# Find duplicate words
duplicateIndices = []
for index in range(1, len(text)):
    if text[index] == text[index - 1]:
        duplicateIndices.append(index)
        
# Remove duplicates
counter = 0
while counter < len(duplicateIndices):
    text.pop(duplicateIndices[counter] - counter)
    counter += 1

# Display results
print('\n'.join(text))
