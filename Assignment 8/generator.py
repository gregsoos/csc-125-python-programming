"""
Program: generator.py
Author: Greg Soos
Last date modified: 04.18.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: Make the following modifications to the original sentence-generator program:
a. The prepositional phrase is optional. (It can appear with a certain
   probability.)
b. A conjunction and a second independent clause are optional: The boy took a
   drink and the girl played baseball.
c. An adjective is optional: The girl kicked the red ball with a sore foot.
You should add new variables for the sets of adjectives and conjunctions.
"""

import random

PREP_PROBABILITY = 0.5     # Probability to include prepositional phrase
ADJ_PROBABILITY = 0.5      # Probability to include adjective
CLAUSE_2_PROBABILITY = 0.5 # Probability to include conjunction and second clause

# Vocabulary: words in different parts of speech
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")
conjunctions = ('AND', 'OR')
adjectives = ('RED', 'BLUE', 'SCARY', 'SMART')

def sentence(PREP_PROBABILITY, ADJ_PROBABILITY, CLAUSE_2_PROBABILITY):
    """Builds and returns a sentence."""
    
    # Condition to include conjunction and second clause
    if random.random() <= CLAUSE_2_PROBABILITY:
        return nounPhrase(ADJ_PROBABILITY) + " " + verbPhrase(PREP_PROBABILITY, ADJ_PROBABILITY) \
               + " " + random.choice(conjunctions) + " " + \
               nounPhrase(ADJ_PROBABILITY) + " " + verbPhrase(PREP_PROBABILITY, ADJ_PROBABILITY)
    
    # Else, return single-clause sentence
    return nounPhrase(ADJ_PROBABILITY) + " " + verbPhrase(PREP_PROBABILITY, ADJ_PROBABILITY)


def nounPhrase(ADJ_PROBABILITY):
    """Builds and returns a noun phrase."""
    
    # Condition to include adjective
    if random.random() <= ADJ_PROBABILITY:
        return random.choice(articles) + " " + random.choice(adjectives) + ' ' + random.choice(nouns)
    
    # Else, do not include adjective   
    return random.choice(articles) + " " + random.choice(nouns)


def verbPhrase(PREP_PROBABILITY, ADJ_PROBABILITY):
    """Builds and returns a verb phrase (with optional prepositional phrase)."""
        
    # Condition to include prepositional phrase
    if random.random() <= PREP_PROBABILITY:
        return random.choice(verbs) + " " + nounPhrase(ADJ_PROBABILITY) + " " + prepositionalPhrase(ADJ_PROBABILITY)
    
    # Else, do not include prepositional phrase
    return random.choice(verbs) + " " + nounPhrase(ADJ_PROBABILITY)


def prepositionalPhrase(ADJ_PROBABILITY):
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase(ADJ_PROBABILITY)


def main():
    """Allows the user to input the number of sentences to generate."""  
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
         print(sentence(PREP_PROBABILITY, ADJ_PROBABILITY, CLAUSE_2_PROBABILITY))

            
# The entry point for program execution
if __name__ == "__main__":
    main()
