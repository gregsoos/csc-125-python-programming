"""
Program: shiftright.py
Author: Greg Soos
Last date modified: 04.04.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: A bit shift is a procedure whereby the bits in a bit string are moved to the left or
to the right. For example, we can shift the bits in the string 1011 two places to
the left to produce the string 1110. Note that the leftmost two bits are wrapped 
around to the right side of the string in this operation. Define two scripts,
shiftLeft.py and shiftRight.py, that expect a bit string as an input. The script
shiftLeft shifts the bits in its input one place to the left, wrapping the leftmost bit
to the rightmost position. The script shiftRight performs the inverse operation.
Each script prints the resulting string.
"""

# Request inputs
binaryString = input('Enter a string of 1s and 0s: ')

# Initialize shifted string and apply bit shift
rightShift = ''
for i in range(len(binaryString)):
    if i == 0: # Wrap-around condition
        rightShift += binaryString[len(binaryString) - 1]
    else:
        rightShift += binaryString[i - 1]

# Display output
print(rightShift)