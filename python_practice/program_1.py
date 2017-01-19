# python practice - program_1.py

from datetime import date

"""Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will
turn 100 years old."""

print '\nWhat\'s your name ?',
name = raw_input('--> ')
print '\nHow old are you, %s?' % name,
age = int(raw_input('-->'))

year = date.today().year + (100 - age)

print '\ngreat %s you become 100 years old in %d' % (name, year)
