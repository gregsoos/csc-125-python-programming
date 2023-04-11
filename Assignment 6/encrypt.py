"""
Program: encrypt.py
Author: Greg Soos
Last date modified: 04.11.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: Write a script that inputs a line of plaintext and a distance value and outputs an
encrypted text using a Caesar cipher. The script should work for any printable
characters.
"""

# Request inputs
plainText = input("Enter a one-line message: ")
distance = int(input("Enter the distance value: "))

# Apply Caesar cipher to message
code = ""
for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue > 127: # Wrap around if end of ASCII set is reached
        cipherValue = cipherValue - 128
    code += chr(cipherValue)

# Display result
print(code)