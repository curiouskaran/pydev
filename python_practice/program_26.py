#python practice - program_26.py
__author__ = 'karan sharma'

'''This exercise is Part 3 of 4 of the Tic Tac Toe exercise series. The other 3 exercises are: Part 1, Part 2, and Part 4.
In a previous exercise we explored the idea of using a list of lists as a data structure to store information about a tic tac toe game.
In a tic tac toe game, the game server needs to know where the Xs and Os are in the board, to know whether player 1 or player 2
(or whoever is X and O won).
There has also been an exercise about drawing the actual tic tac toe gameboard using text characters.
The next logical step is to deal with handling user input. When a player (say player 1, who is X) wants to place an X on the screen,they
cant just click on a terminal. So we are going to approximate this clicking simply by asking the user for a coordinate of where they want
to place their piece.
As a reminder, our tic tac toe game is really a list of lists. The game starts out with an empty game board like this:
game = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]
The computer asks Player 1 (X) what their move is (in the format row,col), and say they type 1,3. Then the game would print out
game = [[0, 0, X],
       [0, 0, 0],
       [0, 0, 0]]
And ask Player 2 for their move, printing an O in that place.
Things to note:
For this exercise, assume that player 1 (the first player to move) will always be X and player 2 (the second player) will always be O.
Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0). To people who dont program,
starting to count at 0 is a strange concept, so it is better for the user experience if the row counts and column counts start at 1. This
is not required, but whichever way you choose to implement this, it should be explained to the player.
Ask the user to enter coordinates in the form row,col - a number, then a comma, then a number. Then you can use your Python skills to
figure out which row and column they want their piece to be in.
Dont worry about checking whether someone won the game, but if a player tries to put a piece in a game position where there already is
another piece, do not allow the piece to go there.'''

import sys
from pandas import *

#intial game state
game = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

#checking and reflecting user input on screen
print'By default player1 uses X and player2 uses O'


def enter_move():
    turn = 0
    moves = 0
    x = 0
    y = 0

    while(moves != 9):
        print DataFrame(game)
        if turn == 0:
            print'enter your move player1(in form of (x,y) coordinates starting form (0,0) to (2,2)) eg-1,2',
            inp = [int(x) for x in raw_input('-->').split(",")]
            x = inp[0]
            y = inp[1]
        elif turn == 1:
            print'enter your move player2(in form of (x,y) coordinates starting form (0,0) to (2,2)) eg-1,2',
            inp = [int(x) for x in raw_input('-->').split(",")]
            x = inp[0]
            y = inp[1]
        try:
            if(turn == 0 and game[x][y] == 0):
                game[x][y] = 'X'
                moves += 1
                turn =1
            elif(turn == 1 and game[x][y] == 0):
                game[x][y] = 'O'
                moves += 1
                turn = 0
            else:
                print'exiting game due to invalid move'
                sys.exit(0)
            print'current game scenario is'

        except IndexError:
            print're-enter input as IndexError occured opps!!'
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."
    return 0
enter_move()

