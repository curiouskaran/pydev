#intial project on classes - turtles

import turtle

def draw_shapes():
	window = turtle.Screen()
	window.bgcolor("pink")
	draw_square()
	draw_circle()
	draw_triangle()
	window.exitonclick()

def draw_square():
	karan = turtle.Turtle()
	karan.shape("turtle")
	karan.color("green")
	karan.speed(2)
	for x in xrange(1,5):
		karan.forward(100)
		karan.right(90)

def draw_circle():
	pass
	khushboo = turtle.Turtle()
	khushboo.shape("circle")
	khushboo.color("blue")
	khushboo.circle(100)

def draw_triangle():
	nanda =turtle.Turtle()
	nanda.shape("arrow")
	nanda.speed(2)
	for y in xrange(1,3):
		nanda.right(60)
		nanda.forward(100)
	nanda.right(150)
	nanda.forward(160)

draw_shapes()
