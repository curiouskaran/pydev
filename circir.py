#draw circle from circles - circir.py

import turtle

def cirsqa():
	window = turtle.Screen()
	window.bgcolor("pink")
	final = turtle.Turtle()
	final.shape("arrow")
	final.color("green")

	for y in range(1,361):
		for x in range(1,5):
			final.circle(100)
		final.right(1)
	window.exitonclick()
cirsqa()



