"""
Program: bouncy.py
Author: Greg Soos
Last date modified: 02.21.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: A standard science experiment is to drop a ball and see how high it bounces.
Once the “bounciness” of the ball has been determined, the ratio gives a bounciness index. 
For example, if a ball dropped from a height of 10 feet bounces 6 feet
high, the index is 0.6, and the total distance traveled by the ball is 16 feet after
one bounce. If the ball were to continue bouncing, the distance after two bounces
would be 10 ft + 6 ft + 6 ft + 3.6 ft = 25.6 ft. Note that the distance traveled for
each successive bounce is the distance to the floor plus 0.6 of that distance as the
ball comes back up. Write a program that lets the user enter the initial height
from which the ball is dropped and the number of times the ball is allowed to
continue bouncing. Output should be the total distance traveled by the ball.
"""

# Initialize bounciness index constant
INDEX = 0.6

# Request inputs
bounceHeight = float(input('Enter the initial height of the ball: ')) # generic units
numberBounces = int(input('Enter the number of times the ball bounces: '))

# Compute total distance traveled and display result
distance = 0
for bounce in range(numberBounces):
    distance += bounceHeight + INDEX * bounceHeight
    bounceHeight *= INDEX # Re-assign to current bounce height
print('Total distance:', distance)