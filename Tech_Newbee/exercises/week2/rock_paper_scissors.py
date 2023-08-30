"""
Implementation of rock, paper, scissors

Read through the entire program to understand what has been done and 
what is left.
Some lines of code have been left empty for you to fill in.

In this game the user is expected to enter one of r/p/s
r for rock
p for paper
s for scissors

After which the computer is going to randomly select one of r/p/s

After user and computer inputs have been selected we need to decide the results of the game

The game is a tie/draw if both select the same thing
The game is won if:
- user selects p, computer selects r
- user selects r, computer selects s
- user selects s, computer selects p

Otherwise, the game is lost.
"""

import random

def play():
    user = #get user input (r/p/s)
    computer = #computer input

    if user == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r

print(play())
