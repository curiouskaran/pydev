import sys
from pandas import *


# python practice - final_game.py
__author__ = 'karan sharma'

'''The next step is to put all these three components together to make a two-player Tic Tac Toe game!
Your challenge in this exercise is to use the functions from those previous
exercises all together in the same program to make a two-player game that
you can play with a friend.There are a lot of choices you will have to make
when completing this exercise, so you can go as far or as little as you want with it.
Here are a few things to keep in mind:
1) You should keep track of who won - if there is a winner, show a
congratulatory message on the screen.
2) If there are no more moves left, dont ask for the next players move!'''

# intial game state
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

print'*******************Welcome to tic-tac-toe game*******************'

# checking and reflecting user input on screen
print'By default player1 uses X and player2 uses O'


def check_who_won(matrix):
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == " x " or matrix[0][-1] == matrix[1][-2] == matrix[2][-3] == " x ":
        return 1

    for i in range(0, 3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] == " x ":
            return 1

    for i in range(0, 3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] == " x ":
            return 1

    if matrix[0][0] == matrix[1][1] == matrix[2][2] == " O " or matrix[0][-1] == matrix[1][-2] == matrix[2][-3] == " O ":
        return 2

    for i in range(0, 3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] == " O ":
            return 2

    for i in range(0, 3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] == " O ":
            return 2
    return 0


def enter_move():
    turn = 0
    moves = 0
    x = 0
    y = 0
    while(check_who_won(game) == 0 and moves != 9):
        print'current game scenario is'
        print DataFrame(game)
        if turn == 0:
            print'''enter your move player1(in form of (x,y) coordinates
                    starting form (0,0) to (2,2)) eg-1,2''',
            inp = [int(x) for x in raw_input('-->').split(",")]
            x = inp[0]
            y = inp[1]
        elif turn == 1:
            print'''enter your move player2(in form of (x,y) coordinates
                    starting form (0,0) to (2,2)) eg-1,2''',
            inp = [int(x) for x in raw_input('-->').split(",")]
            x = inp[0]
            y = inp[1]
        try:
            if(turn == 0 and game[x][y] == 0):
                game[x][y] = 'X'
                moves += 1
                turn = 1
            elif(turn == 1 and game[x][y] == 0):
                game[x][y] = 'O'
                moves += 1
                turn = 0
            else:
                print'exiting game due to invalid move'
                sys.exit(0)

        except IndexError:
            print're-enter input as IndexError occured opps!!'
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."

    if(check_who_won(game) == 1):
        print DataFrame(game)
        print 'player1 wins!!!'
        sys.exit(0)
    elif(check_who_won(game) == 2):
        print DataFrame(game)
        print 'player2 wins!!!'
        sys.exit(0)

    return 0


enter_move()
