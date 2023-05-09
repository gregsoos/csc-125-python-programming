"""
Program:  doctor.py
Author: Greg Soos
Last date modified: 05.08.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

Prompt: In Case Study 5.5, when the patient addresses the therapist personally, 
the therapist’s reply does not change persons appropriately. To see an example of this
problem, test the program with “you are not a helpful therapist.” Fix this problem
by repairing the dictionary of replacements.
"""

import random

hedges = ("Please tell me more.", "Many of my patients tell me the same thing.", "Please continue.")
qualifiers = ("Why do you say that ", "You seem to think that ", "Can you explain why ")
replacements = {"I":"you", "me":"you", "my":"your", "we":"you", "us":"you", "mine":"yours", "am": "are",
                "you": "I", "your": "my", "yours": "mine", "are": "am"}

def reply(sentence):
    """Builds and returns a reply to the sentence."""
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence)


def changePerson(sentence):
    """Replaces first person pronouns with second person pronouns."""
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))
    return " ".join(replyWords)


def main():
    """Handles the interaction between patient and doctor."""
    print("Good morning, I hope you are well today.")
    print("What can I do for you?")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        print(reply(sentence))


# The entry point for program execution
if __name__ == "__main__":
    main()
    