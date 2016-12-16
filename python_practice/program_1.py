#python practice - progrmam 1


"""Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old."""

print '\nWhat\'s your name ?',
name = raw_input('--> ')
print '\nHow old are you, %s?' % name,
age = int(raw_input('-->'))

year = 2016 + (100 -age)

print '\ngreat %s you become 100 years old at %d'%(name, year)