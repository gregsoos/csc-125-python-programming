"""
Program: momentum6.py
Author: Greg Soos
Last date modified: 02.14.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: The kinetic energy of a moving object is given by the formula KE = (1/2)mv^2
where m is the object’s mass and v is its velocity. Modify the program you created
in Project 5 so that it prints the object’s kinetic energy as well as its momentum.
"""

# Request inputs
mass = float(input('Enter the mass in kilograms: '))
velocity = float(input('Enter the velocity in meters per second: '))

# Calculate momentum, kinetic energy and display results
print('The kinetic energy is', (mass * velocity ** 2) / 2, 'J') # K = 1/2 mv^2
print('The momentum is', mass * velocity, 'kg m/s') # p = m / v