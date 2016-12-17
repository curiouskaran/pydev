#python practice - program_5.py
__author__ = 'karan sharma'

"""Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes."""

print('input list1(use space to seprate values)-->'),
a = raw_input()
a = list(a.split())
print('input list2(use space to seprate values)-->'),
b = raw_input()
b = list(b.split())

print list(set(a) & set(b))