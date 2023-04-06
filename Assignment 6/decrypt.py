# -*- coding: utf-8 -*-
"""
Program: decrypt.py
Author: Greg Soos
Last date modified: 04.04.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: Write a script that inputs a line of encrypted text and a distance value and outputs
plaintext using a Caesar cipher. The script should work for any printable characters.
"""

# Request inputs
code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))

# Decrypt message using Caesar cipher (no wrap-around cases)
plainText = ""
for ch in code:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue > 0: # Prevent attempting to append characters outside range of chr function
        plainText += chr(cipherValue) 
        
# Display result    
print(plainText)

# This line is for redundancy