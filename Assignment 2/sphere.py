"""
Program: sphere.py
Author: Greg Soos
Last date modified: 02.06.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: Write a program that takes the radius of a sphere (a 
floating-point number) as input and then outputs the sphere’s 
diameter, circumference, surface area, and volume.
"""

# Request radius
radius = float(input("Enter the sphere's radius: "))

# Calculate diameter, circumference, surface area, volume
diameter = 2 * radius
circumference = 3.14 * diameter
surfaceArea = 4 * 3.14 * (radius ** 2)
volume = 4/3 * 3.14 * (radius ** 3)

# Display results
print("The sphere's diameter is " + str(diameter) + " units")
print("The sphere's circumference is " + str(circumference) + " units")
print("The sphere's surface area is " + str(surfaceArea) + " square units")
print("The sphere's volume is " + str(volume) + " cubic units")