"""
Program: employeepay.py
Author: Greg Soos
Last date modified: 02.14.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: An employee’s total weekly pay equals the hourly wage multiplied by the total
number of regular hours plus any overtime pay. Overtime pay equals the total
overtime hours multiplied by 1.5 times the hourly wage. Write a program that
takes as inputs the hourly wage, total regular hours, and total overtime hours and
displays an employee’s total weekly pay.
"""

# Request inputs
wage = float(input('Enter the hourly wage: '))
regularHours = float(input('Enter the total number of regular hours worked: '))
overtimeHours = float(input('Enter the total number of overtime hours worked: '))

# Calculate total pay and display result
totalPay = (regularHours * wage) + (overtimeHours * wage * 1.5) # see prompt for formula explanation
print("The employee's total weekly pay is", totalPay)