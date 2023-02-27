"""
Program: klickstonauts.py
Author: Greg Soos
Last date modified: 02.14.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: Write a program that takes as input a number of kilometers and prints the 
corresponding number of nautical miles. Use the following approximations:
   
    • A kilometer represents 1/10,000 of the distance between the North Pole and
      the equator.
    • There are 90 degrees, containing 60 minutes of arc each, between the North
      Pole and the equator.
    • A nautical mile is 1 minute of an arc.

"""

# Request a value in kilometers
klicks = float(input('Enter the value in kilometers: '))

# Convert value to nautical miles and display
print('This equals', klicks * 90 * 60 / 10000.0, 'nautical miles') # see above for kilometer to nautical mile conversion