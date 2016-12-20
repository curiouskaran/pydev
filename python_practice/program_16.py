#python practice - program_16.py
__author__ = 'karan sharma'

'''Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters,
 uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new
 password.'''

import string
import random

print'enter length of password',
pass_length = int(raw_input('-->'))
print'enter the strength of password(s for strong,w for weak)',
pass_strength = raw_input('-->')
out = []
status = 1
count = 0

def print_pass(char_set):
    for x in xrange(0,pass_length):
        out.append(random.choice(char_set))
    return ''.join(out)

while status:
    if(pass_strength == 's'):
        char_set = string.printable
        print'The generated password is-->',print_pass(char_set)
        out[:] = []
        print'enter any number to continue the program,enter 0 to exit',
        status = int(raw_input('-->'))
    elif(pass_strength == 'w'):
        char_set = string.ascii_letters
        print'The generated password is-->',print_pass(char_set)
        out[:] = []
        print'enter any number to continue the program,enter 0 to exit',
        status = int(raw_input('-->'))
    else:
        print'please enter a valid input by restarting the program'
        status = 0