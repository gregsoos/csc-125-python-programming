"""
Program: equilateral.py
Author: Greg Soos
Last date modified: 02.21.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is an equilateral
triangle.
"""

# Request triangle side lengths (generic units)
side1 = float(input('Enter the length of the first side: '))
side2 = float(input('Enter the length of the second side: '))
side3 = float(input('Enter the length of the third side: '))

# Determine if equilateral and print result
if side1 == side2 == side3:
    print('The triangle is equilateral!')
else:
    print('The triangle is NOT equilateral.')