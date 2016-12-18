#python practice - program_8.py
__author__ = 'karan sharma'

'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and ask if the players want to start a new game)
Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock'''

print '######################Welcome to the game of Rock-Paper-Scissors######################'

status = 1
while (status == True):
    print'enter your input player1(Rock-Paper-Scissors)',
    inp1 = raw_input('-->')
    print'enter your input player2(Rock-Paper-Scissors)',
    inp2 = raw_input('-->')

    if((inp1 == "Rock" and inp2 == "Scissors")or(inp1 == "Scissors" and inp2 == "Paper")or(inp1 == "Paper" and inp2 == "Rock")):
        print'player1 wins the game'
        print'press any number key to continue or else enter 0 to terminate',
        status = int(raw_input('-->'))
    elif((inp2 == "Rock" and inp1 == "Scissors")or(inp2 == "Scissors" and inp1 == "Paper")or(inp2 == "Paper" and inp1 == "Rock")):
        print'player2 wins the game'
        print'press any number key to continue or else enter 0 to terminate',
        status = int(raw_input('-->'))
    elif(inp1 == inp2):
        print'it is a tie ooo!!'
        print'press any number key to continue or else enter 0 to terminate',
        status = int(raw_input('-->'))
    else:
        print'it is an error please only enter valid input'
        print'press any number key to continue or else enter 0 to terminate',
        status = int(raw_input('-->'))


