"""
Program: proj01.py
Author: Greg Soos
Last date modified: 05.09.2023

Programmed for Bunker Hill Community College's course 
CSC-125-200 Python Programming in the Spring 2023 semester.

This semester project provides a script to play rock, paper, scissors with the user.
The computer learns that the user may have a preferred weapon of choice, and may choose
its response to battle that preference accordingly.
"""

from random import randint

class RockPaperScissors:
    """Allows the user to set up and play a game of rock, paper, scissors against a computer,
    with game history saved and computer able to learn to counter user's preferred weapon."""
    
    def __init__(self):
        """Initialize play structure and result trackers."""
        
        # Initialize list of possible plays, look-up tables for user input and rock-paper-scissors win structure
        self.POSSIBLE_PLAYS = ['ROCK', 'PAPER', 'SCISSORS']
        self.PLAYER_INPUT = {'r': 'ROCK', 'p': 'PAPER', 's': 'SCISSORS'}
        self.WIN_STRUCTURE = {'ROCK': 'PAPER', 'PAPER': 'SCISSORS', 'SCISSORS': 'ROCK'}

        # Initialize counters for number of games, game results, and user's chosen weapons
        self.gameNumber = 1
        self.gameResults = {'WINS': 0, 'LOSSES': 0, 'DRAWS': 0}
        self.userPlays = {'ROCK': 0, 'PAPER': 0, 'SCISSORS': 0}

    
    def generateComputerPlay(self):
        """Generate computer's rock, paper, scissors play based on user's previous choices."""
        
        numUserPlays = list(self.userPlays.values())

        # If player has chosen one weapon the most, computer chooses what beats it
        if numUserPlays.count(max(numUserPlays)) == 1:
            userPreferredPlay = self.POSSIBLE_PLAYS[numUserPlays.index(max(numUserPlays))]
            return self.WIN_STRUCTURE[userPreferredPlay]

        # If player has NOT chosen one weapon the most, computer generates random play
        else:
            return self.POSSIBLE_PLAYS[randint(0, 2)]
    
    
    def playGame(self, userPlay, computerPlay):
        """Determine results of rock, paper, scissors game given a user and a computer's play."""
        
        # COMPUTER WINS
        if self.WIN_STRUCTURE[self.PLAYER_INPUT[userPlay.lower()]] == computerPlay:
            print(f'The computer played {computerPlay.lower()}.\nYou lose.\n')
            self.gameNumber += 1 # Update game counter        
            self.gameResults['LOSSES'] += 1 # Update game result counter
            self.userPlays[self.PLAYER_INPUT[userPlay.lower()]] += 1 # Update user weapon choice counter

        # USER WINS
        elif self.WIN_STRUCTURE[computerPlay] == self.PLAYER_INPUT[userPlay.lower()]:
            print(f'The computer played {computerPlay.lower()}.\nYou win!\n')
            self.gameNumber += 1
            self.gameResults['WINS'] += 1
            self.userPlays[self.PLAYER_INPUT[userPlay.lower()]] += 1

        # USER AND COMPUTER TIE
        else:
            print(f'The computer played {computerPlay.lower()}.\nYou tie.\n')
            self.gameNumber += 1
            self.gameResults['DRAWS'] += 1
            self.userPlays[self.PLAYER_INPUT[userPlay.lower()]] += 1

                
    def getResults(self):
        """Print times user won, lost, and tied the game."""
        for key in self.gameResults:
            print(f'{key}: {self.gameResults[key]}')
    
    
    def getUserPlays(self):
        """Print the number of times the user played each weapon."""
        for key in self.userPlays:
            print(f'You played {key} {self.userPlays[key]} times.')
            
            
def main():
    """Play a rock, paper, scissors game until the user enters 'q' or 'Q' to quit."""
    
    game = RockPaperScissors()
    userPlay = '' # Initialize
    while userPlay.lower() != 'q':
        
        # Computer chooses weapon
        computerPlay = game.generateComputerPlay()
        
        # User chooses weapon or to quit 
        while True:
            userPlay = input(f'Round {game.gameNumber}! Choose your play: ')
            if (userPlay.lower() == 'r' 
                    or userPlay.lower() == 'p' 
                    or userPlay.lower() == 's'
                    or userPlay.lower() == 'q'):
                break
            else:
                print('Incorrect value. Please enter "r", "p", "s", or "q" in lower or upper case.\n')
        
        # Game is played if user has chosen weapon
        if (userPlay.lower() == 'r' 
                or userPlay.lower() == 'p' 
                or userPlay.lower() == 's'):
            game.playGame(userPlay, computerPlay)     
            
    print(f'\nCongrats! You played {game.gameNumber - 1} times!')
    game.getResults()
    game.getUserPlays()

    
if __name__ == '__main__':
    main()
    