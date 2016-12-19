#python practice - program_11.py
__author__ = 'karan sharma'

'''Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).'''

print'enter a number',
num = int(raw_input('-->'))
result_list = []

def is_prime():
    for divisor in xrange(2 ,num):
        if(num % divisor == 0):
            result_list.append(divisor)
    if num == 1:
        print'it is not prime number by default'
    elif not result_list:
        print'yay!! it a prime number'
    else:
        print'it is not a prime number'

is_prime()