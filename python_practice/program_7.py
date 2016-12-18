#python practice - program_7.py
__author__ = 'karan sharma'

"""Lets say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it."""

print'enter a list of numbers(use space to seperate numbers)',
num_list = [int(x) for x in raw_input().split()]
final_list = [element for element in num_list if(element % 2 == 0)]

print list(set(final_list))
