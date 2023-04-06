# -*- coding: utf-8 -*-
"""
Program: encrypt.py
Author: Greg Soos
Last date modified: 04.04.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: Write a script that inputs a line of plaintext and a distance value and outputs an
encrypted text using a Caesar cipher. The script should work for any printable
characters.
"""

# Request inputs
plainText = input("Enter a one-line message: ")
distance = int(input("Enter the distance value: "))

# Apply Caesar cipher to message (no wrap-around case)
code = ""
for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    code += chr(cipherValue)

# Display result
print(code)

# A line to prevent potential duplicate error