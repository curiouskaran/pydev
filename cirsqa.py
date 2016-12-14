#draw circle from squares - cirsqa.py

import turtle

def cirsqa():
	window = turtle.Screen()
	window.bgcolor("pink")
	final = turtle.Turtle()
	final.shape("arrow")
	final.color("green")

	for y in range(1,361):
		#for x in range(1,5):
			#final.forward(100)
			#final.right(90)
		radius = 100
		final.circle(radius)
		radius = radius + 50
		final.right(50)
	window.exitonclick()
cirsqa()



