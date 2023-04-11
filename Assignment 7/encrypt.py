"""
Program: encrypt.py
Author: Greg Soos
Last date modified: 04.11.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: Use the strategy of the decimal to binary conversion and the bit shift left operation
defined in Project 5 to code a new encryption algorithm. The algorithm
should add 1 to each character’s numeric ASCII value, convert it to a bit string,
and shift the bits of this string one place to the left. A single-space character in
the encrypted string separates the resulting bit strings. 
"""

# Request inputs
plainText = input("Enter a one-line message: ")

# Apply encryption method and display result
for ch in plainText:
   
    if ord(ch) == 127: # Wraps around to 0
        print('0', end = ' ')
    
    else:
        # Apply Caesar cipher to character
        cipherValue = ord(ch) + 1
        
        # Convert ASCII value of character to binary
        bitString = ""
        while cipherValue > 0:
            remainder = cipherValue % 2
            cipherValue = cipherValue // 2
            bitString = str(remainder) + bitString

        # Initialize shifted string and apply bit shift
        leftShift = ''
        for i in range(len(bitString)):
            if i == (len(bitString) - 1): # Wrap-around condition
                leftShift += bitString[0]
            else:
                leftShift += bitString[i + 1]
                
        # Print result
        print(leftShift, end = ' ')