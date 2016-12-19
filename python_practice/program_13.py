#python practice - program_13.py
__author__ = 'karan sharma'

'''Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence
to generate.
(Hint The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in
the sequence.'''
print'enter the first number in the series',
start = int(raw_input('-->'))
print'enter the number upto which fibonnaci sequence required',
end = int(raw_input('-->'))


def fibonnaci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)
print [ fibonnaci(n) for n in xrange(start,end) ]