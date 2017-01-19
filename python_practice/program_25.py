#python practice - program_25.py
__author__ = 'karan sharma'

'''This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other 3 exercises are: Part 1, Part 3, and Part 4.
In a previous exercise we drew a Tic Tac Toe board. As you may have guessed, we are trying to build up to a full tic-tac-toe board.
However, this is significantly more than half an hour of coding, so were doing it in pieces.
Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.
If a game of Tic Tac Toe is represented as a list of lists, like so:
game = [[1, 2, 0],
       [2, 1, 0],
       [2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in
that space.
Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me
which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Dont worry about the case where
TWO people have won - assume that in every board there will only be one winner.'''

print'*****************************************Welcome to tic-tac-toe game*****************************************'

# take input from user in one row
print'enter a game scenario in row major order(3x3 matrix)',
nn_matrix = [int(x) for x in raw_input('-->').split()]
total_cells =  len(nn_matrix)
# calculate 'n'
row_cells = int(total_cells**0.5)
# calculate rows
matrix = [nn_matrix[i:i+row_cells] for i in range(0, total_cells, row_cells)]


def check_grid(grid):
    #rows
    for x in xrange(0,2):
        row = set([grid[0][x],grid[1][x],grid[2][x]])
        if len(row) == 1 and grid[x][0] != 0:
            return grid[x][0]
    #column
    for x in xrange(0,3):
        col = set([grid[0][x],grid[1][x],grid[2][x]])
        if len(col) == 1 and grid[0][x] != 0:
            return grid[0][x]
    #diagonals
    diag1 = set([grid[0][0],grid[1][1],grid[2][2]])
    diag2 = set([grid[0][2],grid[1][1],grid[2][0]])
    if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
        return grid[1][1]

    return 0


'''matrix = [['x', 'x', 'x'],
         ['x', 'y', 'y'],
         ['y', 'y', 'x']]'''
print check_grid(matrix)

