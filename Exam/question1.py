"""
Author: Greg Soos
File: question1.py
Last modified: 3/28/2023

Prompt: 
Q 1. The Body Mass Index, BMI, is calculated as
BMI =703w/h**2 ;
where w is the person’s weight in pounds and 'h' is the person’s height in inches. Write a program that
asks the user for their height their weight and prints out their BMI. 
"""

# Request inputs
weight_lb = float(input('Please enter your weight: '))
height_in = float(input('Please enter your height: '))

# Calculate BMI and display result
bmi = 703 * weight_lb / (height_in**2)
print('Your BMI is', "%0.2f" % bmi) # Display to two digits of precision