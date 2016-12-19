#python_practice -program_14.py
__author__ = 'karan sharma'

'''Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all
the duplicates.'''

def rm_duplicate():
    not_dup = list(set(int(element) for element in raw_input('enter a list(all element sperated by space)-->').split()))
    return not_dup

print rm_duplicate()

