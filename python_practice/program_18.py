#python practice - program_18.py
__author__ = 'karan sharma'

'''the player try to guess the opponents number(computer here) who gives the number. If the matching digits are in their right
positions, they are "bulls", if in different positions, they are "cows". Example:
Secret number: 4271
Opponent's try: 1234
Answer: 1 bull and 2 cows. (The bull is "2", the cows are "4" and "1".)'''

import random,sys

print'#######################################Welcome to the Cows and Bulls Game!#######################################'

rand_target = list(str(random.randint(1000,9999)))
cows = 0
bulls = 0
while bulls != 4:
    bulls = 0
    cows = 0
    print'Enter the guess(4 digit number only)',
    inp = list(raw_input('-->'))
    if len(inp) == 4:
        for i in xrange(0,4):
            for j in xrange(0,4):
                if rand_target[i] == inp[j]:
                    if i == j:
                        bulls += 1
                    else:
                        cows +=1
        print 'cows-->',cows
        print'bulls-->',bulls
    else:
        print'restart the game you have entered wrong input'
        sys.exit(0)