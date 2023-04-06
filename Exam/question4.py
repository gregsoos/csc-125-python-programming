"""
Author: Greg Soos
File: question4.py
Last modified: 3/28/2023

Prompt: 
Q 4. Write a program that takes the radius of a sphere (a floating-point number) as 
input and then outputs the sphere’s diameter, circumference, surface area, and volume.
"""

from math import pi

# Request input
radius = float(input('Please enter the radius of the sphere: '))

# Calculate outputs
diameter = 2 * radius
circumference = 2 * pi * radius
surfaceArea = 4 * pi * (radius ** 2)
volume = 4/3 * pi * (radius ** 3)

# Display outputs
print('The diameter is', diameter)
print('The circumference is', circumference)
print('The surface area is', surfaceArea)
print('The volume is', volume)