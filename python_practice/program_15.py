#python practice - program_15.py
__author__ = 'karan sharma'

'''Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.
For example, say I type the string:
  My name is Michele
Then I would see the string:
  Michele is name My
shown back to me.'''


def sentence_rev():
    print'enter a english sentence',
    sentence = list(raw_input('-->').split())
    return sentence[::-1]


print ' '.join(sentence_rev())
