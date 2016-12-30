#python_practice - program23.py
__author__ = 'karan sharma'

'''Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime
numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.'''

primes = [line.rstrip('\n') for line in open('prime_numbers.txt')]
happy = [line.rstrip('\n') for line in open('happy_numbers.txt')]

common = [set(primes) & set(happy)]
print common