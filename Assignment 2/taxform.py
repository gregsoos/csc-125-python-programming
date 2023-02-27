"""
Program: taxform.py
Author: Greg Soos
Last date modified: 02.06.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: The tax calculator program of the case study outputs a 
floating-point number that might show more than two digits of precision. 
Use the round function to modify the program to display at most two 
digits of precision in the output number.

The purpose of this program is to calculate one's income tax given
simple tax law (flat tax rate, standard deduction plus an additional
deduction per dependent) It will query the user for their gross income
and number of dependents, then calculate their taxable income by
subtracting the total deduction from their gross. Then, finally, it will
apply the tax rate to the taxable income to determine the income tax.
"""

# Initialize constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

# Request gross income, number of dependents
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

# Compute income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * numDependents
incomeTax = round(taxableIncome * TAX_RATE, ndigits = 2)

# Display result
print("The income tax is $" + str(incomeTax))