#program to check profanity in a given file

import urllib

def read_text():
	fname = raw_input("enter a file:-")
	quotes = open('%s.txt' % fname,'r')
	content_of_file = quotes.read()
	quotes.close()
	profanity_check(content_of_file)

def profanity_check(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	output = connection.read()
	connection.close()
	if "true" in output:
		print("profanity alert!!!")
	elif "false" in output:
		print("document is free from any curse words")
	else:
		print("can't able to check the document please try again") 
read_text()