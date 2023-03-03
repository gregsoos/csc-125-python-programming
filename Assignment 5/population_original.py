"""
Program: population.py
Author: Greg Soos
Last date modified: 02.28.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: A local biologist needs a program to predict population growth. The inputs
would be the initial number of organisms, the rate of growth (a real number
greater than 0), the number of hours it takes to achieve this rate, and a number
of hours during which the population grows. For example, one might start with a
population of 500 organisms, a growth rate of 2, and a growth period to achieve
this rate of 6 hours. Assuming that none of the organisms die, this would imply
that this population would double in size every 6 hours. Thus, after allowing
6 hours for growth, we would have 1000 organisms, and after 12 hours, we would
have 2000 organisms. Write a program that takes these inputs and displays a prediction 
of the total population.

Predict population growth, assuming that no organisms die.

Inputs:
   initial number of organisms
   rate of growth (a float > 1)
   the number of hours to achieve the rate
   number of hours of growth

Outputs:
Total population in int format.

The formula for this calculation is:
Final # of organisms = initial # of organisms * (growth rate ** (total time / time to achieve growth rate))

In the example given, this would then be:
Final # of organisms = 500 * (2 ** (12 hrs / 6 hrs)) = 500 * (2 ** 2) = 500 * 4 = 2000

So in a loop, with each pass we iterate by an hour and can think of ourselves as multiplying the current
number of organisms by a factor of the growth rate ** (1 / time to achieve growth rate). Iterated over whatever
amount of total time we want, this simply equates to the formula given above. 

"""

# Request inputs
amtOrganism = int(input('Enter the initial number of organisms: '))
growthRate = float(input('Enter the rate of growth: '))
timeToAchieveRate = int(input('Enter the number of hours it takes to achieve the growth rate: '))
totalGrowthTime = int(input('Enter the number of hours during which the population grows: '))

# Calculate total population after given amount of growth time and display result
for hour in range(1, totalGrowthTime + 1):
    amtOrganism *= (growthRate ** (1 / timeToAchieveRate)) # See docstring for formula explanation
print('The total population will be', int(round(amtOrganism)))