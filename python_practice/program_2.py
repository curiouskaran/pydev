#python practice - program_2.py

"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
If the number is a multiple of 4, print out a different message."""

print 'enter a number',
num = int(raw_input("-->"))

if (num % 2 == 0):
    if (num % 4 == 0):
        print("wow!! today is your lucky day you got multiple of 4")
    else:
        print("you got an even number baby!!")
else:
    print("boo!! this is an odd number")
