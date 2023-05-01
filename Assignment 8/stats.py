"""
Program: stats.py
Author: Greg Soos
Last date modified: 05.01.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: A group of statisticians at a local college has asked you to create a set of functions
that compute the median and mode of a set of numbers, as defined in Section
5.4. Define these functions in a module named stats.py. Also include a function
named mean, which computes the average of a set of numbers. Each function
should expect a list of numbers as an argument and return a single number. Each
function should return 0 if the list is empty. Include a main function that tests the
three statistical functions with a given list.
"""

def median(x : list):
    """Computes the median for a list of numbers."""
    
    # If list is empty, return 0; otherwise, sort list numerically and find midpoint
    if x == []:
        return 0
    x.sort()
    midpoint = len(x) // 2
    
    # Compute median (for even number of elements)
    if len(x) % 2 == 1:
        return x[midpoint]
    
    # Else, compute median (for odd number of elements--average two middle elements)
    return (x[midpoint] + x[midpoint - 1]) / 2


def mode(x : list):
    """Computes the mode for a list of numbers."""
    
    # If list is empty, return 0
    if x == []:
        return 0
    
    # Else, compute mode
    x.sort()
    mode = []
    maxFrequency = 0
    for i in x:
        
        # New assignment for mode if new value found that occurs most
        if x.count(i) > maxFrequency:
            mode = [str(i)] 
            maxFrequency = x.count(i)
            
        # Add another value for mode if new value found that occurs same amount as previous
        elif x.count(i) == maxFrequency and mode[len(mode) - 1] != str(i):
            mode.append(str(i))
    
    # Only one element in list, i.e. only one value occurs the most
    if len(mode) == 1: 
        return mode.pop()
    
    # Two or more values occur the same amount, so both are the mode
    else: 
        return ', '.join(mode)
    
    
def mean(x : list):
    """Computes the mean for a list of numbers."""
    
    # If list is empty, return 0
    if x == []:
        return 0
    
    # Else, compute mean
    return sum(x) / len(x)
    
    
def main():
    """Takes a list of numbers as input and displays its mean, median, and mode."""
    
    # Build list of numbers
    x = []
    while True:
        nextNum = input('Please enter a number: ')
        if nextNum == '':
            break
        x.append(float(nextNum))
       
    # Compute mean, median, and mode, and display
    med = median(x); mod = mode(x); avg = mean(x)
    print(f'The median is {med}.')
    print(f'The mode is {mod}.')
    print(f'The mean is {avg}.')

    
if __name__ == "__main__":
    main()
    