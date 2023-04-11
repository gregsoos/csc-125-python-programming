"""
Program: dif.py
Author: Greg Soos
Last date modified: 04.11.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: Write a script named dif.py. This script should prompt the user for the names
of two text files and compare the contents of the two files to see if they are the
same. If they are, the script should simply output "Yes". If they are not, the script
should output "No", followed by the first lines of each file that differ from each
other. The input loop should read and compare lines from each file. The loop
should break as soon as a pair of different lines are found.
"""

# Take the inputs
fileName1 = input("Enter the name of the first file: ")
fileName2 = input("Enter the name of the second file: ")

# Open both files
file1 = open(fileName1, 'r')
file2 = open(fileName2, 'r')

# Check line-by-line if files are the same
while True:
    line1 = file1.readline()
    line2 = file2.readline()
    
    # Determine files are not the same
    if line1 != line2:
        print('No')
        print(line1, end = '')
        print(line2, end = '')
        break
    
    # Determine files are the same
    if line1 == line2 == "":
        print('Yes')
        break