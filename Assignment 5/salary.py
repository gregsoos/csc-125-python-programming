"""
Program: salary.py
Author: Greg Soos
Last date modified: 02.28.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: Teachers in most school districts are paid on a schedule that provides a salary
based on their number of years of teaching experience. For example, a beginning
teacher in the Lexington School District might be paid $30,000 the first year. For
each year of experience after this first year, up to 10 years, the teacher receives a
2% increase over the preceding value. Write a program that displays a salary schedule, 
in tabular format, for teachers in a school district. The inputs are the starting
salary, the percentage increase, and the number of years in the schedule. Each row
in the schedule should contain the year number and the salary for that year.

Compute a school district's salary schedule.

Inputs 
   starting salary
   annual percentage increase
   number of years for which to print the schedule

Outputs
    Two columns containing the year and the salary
    after the increase.
    
"""

# Request inputs
salary = float(input('Enter the starting salary: '))
annualIncrease = float(input('Enter the annual percentage salary increase (e.g. for 5%, enter "5"): '))
totalYears = int(input('Enter the number of years to calculate: '))

# Format columns, calculate salaries, display results
print('%0s%14s' % ('Year', 'Salary')) # Allocate reasonable space to left side of 'Salary' string for column separation
for year in range(1, totalYears + 1):
    print('%4d%14.2f' % (year, salary)) # Right-justify year number and salary (to nearest cent) to respective column
    salary *= 1 + (annualIncrease * 0.01) # Change percent increase to correct decimal value and apply to salary
    salary = round(salary, 2) # Round salary to nearest cent (asssume next increase will be calculated from this)