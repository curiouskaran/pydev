#python practice - program_4.py
__author__ = 'karan sharma'

"""Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don not know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)"""


print("enter a number"),
num = int(raw_input('-->'))

for divisor in xrange(2,num+1):
    if( num % divisor == 0):
        print'%d is a divisor of %d'%(divisor,num)
    y = y + 1