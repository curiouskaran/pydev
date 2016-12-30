#:python practice - program_20.py
__author__ = 'karan sharma'

'''Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest)
and another number using binary search. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate
boolean.'''

import math

print'enter an ordered list (incresing or decresing)',
inp = [int(element) for element in raw_input('-->').split()]
print'enter an element to search in list',
key = int(raw_input('-->'))

i=0
j=len(inp) - 1
def bin_search(i,j,key):
    if(j == i):
        if(inp[i] == key):
            print "key is found hurray!!"
        else:
            print "no that key is not present can/'t you see"
    else:
        mid = int(math.floor((i+j)/2))
        if(inp[mid] == key):
            print "key is found hurray!!"
        else:
            if(key > inp[mid]):
                bin_search(mid + 1,j,key)
            elif(key < inp[mid]):
                bin_search(i,mid - 1,key)

print bin_search(i,j,key)


