#this is intial program for my udacity course - Take a break

import time
import webbrowser

hour_count = 0

print ("this program started on" + time.ctime())
while(hour_count <= 2):
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=9mQJaXwGPlg")
	hour_count = hour_count + 1