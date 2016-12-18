#python practice - program_6.py
__author__ = 'karan sharma'

"""Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)"""

print 'enter a string',
inp = raw_input("-->")

l = len(inp)
r_inp = inp[l:-(l + 1):-1]
if(inp == r_inp):
    print 'it is a pallindrome'
else:
    print 'bummer!! it is not a pallindrome'