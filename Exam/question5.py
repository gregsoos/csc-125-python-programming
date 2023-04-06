"""
Author: Greg Soos
File: question5.py
Last modified: 3/28/2023

Prompt:
Q 5. Write a program where the user gives input in the string format and LETTERS in the string appear in the same line.

i.e
word = input('Enter a word: ')
use a for loop:
         print output in the same line
"""

# Request word
word = input('Enter a word: ')

# Print word using for loop
for letter in word:
    print(letter, end = '')