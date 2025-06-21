import turtle
import tkinter
from turtle import *
from random import randint


turtle.title('Pythagoras Tree')
window = turtle.Screen().bgcolor("#000000")
turtle.screensize()
turtle.setup(width=1.0,height=0.9)
turtle.Turtle()

turtle.hideturtle()
turtle.speed(100)
MIN_DEPTH = 1
height = 280

levels = int(turtle.numinput("Pythagoras Tree", "Quantity of Iterations: ", 8, minval=2, maxval=19))
if levels > 15:
    height+=100

turtle.pensize(levels)
turtle.sety(-250)
turtle.color("#FFFFFF")

turtle.left(90)
turtle.penup()
turtle.backward(height)
turtle.pendown()
turtle.forward(height)
angle = 45


def draw(height,iterations):
    width=turtle.pensize()

    turtle.pensize(3/4*width)
    height = height/(2**0.5)

    turtle.left(angle)
    turtle.forward(height)
    if iterations < levels:
        draw(height, iterations + 1)
    turtle.backward(height)
    turtle.right(2*angle)
    turtle.forward(height)

    if iterations < levels:
        draw(height, iterations + 1)
    turtle.backward(height)
    turtle.left(angle)
    turtle.pensize(width)


draw(height,2)
done()