"""
Program: momentum5.py
Author: Greg Soos
Last date modified: 02.14.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: An object’s momentum is its mass multiplied by its velocity. Write a program
that accepts an object’s mass (in kilograms) and velocity (in meters per second) as
inputs and then outputs its momentum.
"""

# Request inputs
mass = float(input('Enter the mass in kilograms: '))
velocity = float(input('Enter the velocity in meters per second: '))

# Calculate momentum and display result
print('The momentum is', mass * velocity, 'kg m/s') # p = m / v