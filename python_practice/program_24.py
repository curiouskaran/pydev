#python practice - program_24.py
__author__ = 'karan sharma'

'''This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other 3 exercises are: Part 2, Part 3, and Part 4.
Time for some fake graphics! Lets say we want to draw game boards that look like this:
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- --- '''

import math
print'enter the size of grid for tic-tac-toe',
size = int(raw_input('-->'))

for i in xrange(0,size):
    print' ---' * (size)
    print'{} {}'.format('|','  ')*(size +1)

print' ---' * (size)