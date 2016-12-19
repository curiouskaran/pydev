#python practice - program_12.py
__author__ = 'karan sharma'

'''Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
the first and last elements of the given list. For practice, write this code inside a function.'''

num_list = [int(elements) for elements in raw_input('enter a list of numbers(include space to enter next number-->)').split()]

def new_list():
    return [num_list[0],num_list[-1]]

print new_list()