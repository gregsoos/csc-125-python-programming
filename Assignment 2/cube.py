"""
Program: cube.py
Author: Greg Soos
Last date modified: 02.06.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: You can calculate the surface area of a cube if you know the 
length of an edge. Write a program that takes the length of an edge 
(an integer) as input and prints the cube’s surface area as output.
"""

# Request side length
sideLength = int(input("Enter the cube's side length: "))

# Calculate surface area
surfaceArea = 6 * (sideLength ** 2)

# Display result
print("The cube's surface area is " + str(surfaceArea) + " square units")