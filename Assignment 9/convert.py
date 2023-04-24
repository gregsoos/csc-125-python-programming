"""
Program: convert.py
Author: Greg Soos
Last date modified: 04.24.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: Define a function decimalToRep that returns the representation of an integer in a
given base. The two arguments should be the integer and the base. The function
should return a string. It should use a lookup table that associates integers with
digits. Include a main function that tests the conversion function with numbers
in several bases.
"""

# Initialize integer value table
INTEGER_VALUE_TABLE = {}
for i in range(0, 10):
    INTEGER_VALUE_TABLE[i] = str(i) # 0 to 10
for i in range(10, 16):
    INTEGER_VALUE_TABLE[i] = chr(i + 55) # A to F
    
def decimalToRep(integer : str, base : int):
    """Converts an integer to its equivalent value in another base."""
    
    # Return 0 for an entry of 0
    if int(integer) == 0:
        return '0'
    
    # Calculate value otherwise
    quotient = int(integer)
    intInBase = ''
    while quotient:
        intInBase = INTEGER_VALUE_TABLE[quotient % base] + intInBase # Go digit-by-digit adding to digit string
        quotient = quotient // base 
    return intInBase


def main():
    """Accepts integer and base inputs to convert to another base."""
    while True:
        integer = input('Please enter an integer to convert to a given base: ')
        if integer == '': # Exit condition
            break
        base = int(input('Please enter a base to convert to: '))
        print(decimalToRep(integer.upper(), base), end = '\n\n')
   
    
if __name__ == '__main__':
    main()
