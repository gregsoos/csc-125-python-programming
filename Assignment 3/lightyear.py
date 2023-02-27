"""
Program: lightyear.py
Author: Greg Soos
Last date modified: 02.14.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: Light travels at 3 * 10^8 meters per second. A light-year is the distance a light beam
travels in one year. Write a program that calculates and displays the value of a
light-year.
"""

# Calculate/initialize constants (speed of light, seconds in year)
RATE = 3 * 10 ** 8 # meters per second
SECONDS_IN_YEAR = 365 * 24 * 60 ** 2 # days times hours times minutes times seconds

# Calculate length of light-year and display result
print('One light-year is', RATE*SECONDS_IN_YEAR, 'meters') # distance (1 ly) = velocity (c) * time (1 yr)