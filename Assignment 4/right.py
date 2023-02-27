"""
Program: right.py
Author: Greg Soos
Last date modified: 02.21.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is a right triangle. 
Recall from the Pythagorean theorem that in a right triangle, the square of
one side equals the sum of the squares of the other two sides.
"""

# Request triangle side lengths (generic units)
side1 = float(input('Enter the length of the first side: '))
side2 = float(input('Enter the length of the second side: '))
side3 = float(input('Enter the length of the third side: '))

# Determine if right triangle and print result (must account for fact that user may enter side lengths in any order)
if side1 ** 2 == (side2 ** 2) + (side3 ** 2):
    print('The triangle is a right triangle!')
elif side2 ** 2 == (side1 ** 2) + (side3 ** 2):
    print('The triangle is a right triangle!')
elif side3 ** 2 == (side1 ** 2) + (side2 ** 2):
    print('The triangle is a right triangle!')
else:
    print('The triangle is NOT a right triangle.')