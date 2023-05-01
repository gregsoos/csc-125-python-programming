"""
Program: convert.py
Author: Greg Soos
Last date modified: 04.18.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: In Chapter 4, we developed an algorithm for converting from binary to decimal. 
You can generalize this algorithm to work for a representation in any base.
Instead of using a power of 2, this time you use a power of the base. Also, you use
digits greater than 9, such as A . . . F, when they occur. Define a function named
repToDecimal that expects two arguments, a string, and an integer. The second
argument should be the base. For example, repToDecimal("10", 8) returns
8, whereas repToDecimal("10", 16) returns 16. The function should use a
lookup table to find the value of any digit. Make sure that this table (it is actually
a dictionary) is initialized before the function is defined. For its keys, use the 10
decimal digits (all strings) and the letters A . . . F (all uppercase). The value stored
with each key should be the integer that the digit represents. 
(The letter 'A' associates with the integer value 10, and so on.) The main loop of the function should
convert each digit to uppercase, look up its value in the table, and use this value
in the computation. Include a main function that tests the conversion function
with numbers in several bases.
"""

# Initialize digit value table
DIGIT_VALUE_TABLE = {}
for i in range(0, 10):
    DIGIT_VALUE_TABLE[str(i)] = i # 0 to 10
for i in range(10, 16):
    DIGIT_VALUE_TABLE[chr(i + 55)] = i # A to F
    
def repToDecimal(numInBase : str, base : int):
    """Converts a value in a given numeric base to its decimal equivalent."""
    decimal = 0
    exponent = len(numInBase) - 1
    for digit in numInBase:
        decimal += DIGIT_VALUE_TABLE[digit] * base ** exponent
        exponent = exponent - 1
    return decimal


def main():
    """Accepts value and base inputs to convert to decimal."""
    while True:
        numInBase = input('Please enter a value to convert to decimal: ')
        if numInBase == '': # Exit condition
            break
        base = int(input('Please enter a base from which to convert that value: '))
        print(repToDecimal(numInBase.upper(), base), end = '\n\n')

   
if __name__ == '__main__':
    main()
