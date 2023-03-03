"""
Program: gcd.py
Author: Greg Soos
Last date modified: 03.01.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: The greatest common divisor of two positive integers, A and B, is the largest
number that can be evenly divided into both of them. Euclid’s algorithm can be
used to find the greatest common divisor (GCD) of two positive integers. You
can use this algorithm in the following manner:
a.  Compute the remainder of dividing the larger number by the smaller
    number.
b.  Replace the larger number with the smaller number and the smaller number
    with the remainder.
c.  Repeat this process until the smaller number is zero.
    The larger number at this point is the GCD of A and B. Write a program that lets
    the user enter two integers and then prints each step in the process of using the
    Euclidean algorithm to find their GCD.
    
Compute and print the greatest common divisor of two input
integers. and Use while loop.

"""

# Request inputs
integer1 = int(input('Enter a positive integer: '))
integer2 = int(input('Enter a second positive integer: '))

# Calculate GCD using Euclidean algorithm, print numbers/remainders step-by-step and display final result
if integer2 > integer1: # Using if-statement for input generality since remainder has to be calculated in certain order
    while integer1 != 0:
        remainder = integer2 % integer1
        integer2 = integer1
        integer1 = remainder
        print('The smaller number is', integer2, 'and the remainder is', integer1)
    print('The GCD is', integer2)

elif integer2 < integer1:
    while integer2 != 0:
        remainder = integer1 % integer2
        integer1 = integer2
        integer2 = remainder
        print('The smaller number is', integer1, 'and the remainder is', integer2)
    print('The GCD is', integer1)

else: # If the two integers are equal, then they are the greatest common divisor
    print('The GCD is', integer1)