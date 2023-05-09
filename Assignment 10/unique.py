"""
Program: unique.py
Author: Greg Soos
Last date modified: 05.08.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: A file concordance tracks the unique words in a file and their frequencies. Write
a program that displays a concordance for a file. The program should output the
unique words and their frequencies in alphabetical order. Variations are to track
sequences of two words and their frequencies, or n words and their frequencies.
"""

# Take the inputs
fileName = input("Enter the name of the file: ")
while True:
    sequenceLength = input('What word sequence length would you like to track? ')
    try:
        sequenceLength = int(sequenceLength)
        break
    except ValueError:
        print('Please enter an integer.\n')

# Open text file, read and split into a list
inputFile = open(fileName, 'r')
text = inputFile.read()
if not text.isalpha(): # Remove punctuation if necessary
    textOnlyWords = ''
    for character in text:
        if character.isalpha() or character.isspace():
            textOnlyWords += character
    text = textOnlyWords
text = text.split()

# Build list of sequences (if not searching individual words)
if sequenceLength > 1:
    sequences = []
    for numWordInText in range(len(text) - sequenceLength + 1):
        currentSequence = ''
        for numWordInSequence in range(sequenceLength):
            currentSequence += f' {text[numWordInText + numWordInSequence]}' 
        sequences.append(currentSequence.lstrip())
    text = sequences

# Make all words lower-case and alphabetize
for index in range(len(text)):
    text[index] = text[index].lower()  
text.sort()

# Find duplicate words
duplicateInstances = {text[0] : 1} # Words and number duplicates stored as dict
for index in range(1, len(text)):
    
    # Start counter for new word
    if text[index] != text[index - 1]:
        duplicateInstances[text[index]] = 1
    
    # Add to counter for a given word when duplicate found
    else:
        duplicateInstances[text[index]] += 1

# Display results
for word in duplicateInstances:
    print(f'{word.upper()} appears {duplicateInstances[word]} time(s).')
    