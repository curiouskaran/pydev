#python practice - program_9.py
__author__ = 'karan sharma'

'''Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)'''

from random import randint

print'###########################Try your luck game###########################'

status = 1

while(status == True):
    print'enter a number(0-9)',
    guess =int(raw_input('-->'))
    random_number = randint(0,9)
    if(guess == random_number):
        print'Great!! Exactly Right'
        print'To check your luck again enter any number(1-9),press 0 to exit',
        status = int(raw_input('-->'))
    elif(guess < random_number):
        print'Boo!! Too Low'
        print'To check your luck again enter any number(1-9),press 0 to exit',
        status = int(raw_input('-->'))
    elif(guess > random_number):
        print'Boo!! Too High'
        print'To check your luck again enter any number(1-9),press 0 to exit',
        status = int(raw_input('-->'))
    else:
        print'please enter a valid input'
        print'To check your luck again enter any number(1-9),press 0 to exit',
        status = int(raw_input('-->'))
