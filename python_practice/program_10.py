#python practice - program_10.py
__author__ = 'karan sharma'

'''Take two lists, say for example these two:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension.
(Hint: Remember list comprehensions from Exercise 7).'''

def input_list(list_name = 'list'):
    return [ int(element) for element in raw_input('enter elements in  %s (with each number seprated by space)-->'%list_name).split() ]

list1 = input_list('list1')
list2 = input_list('list2')

print list(set(list1) & set(list2))