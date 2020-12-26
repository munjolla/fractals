from turtle import *
speed(0)

def sierpinski(lenght, depth):
    if depth ==0:
        return
    else:
        for i in range(0,3):
            forward(lenght)
            sierpinski(lenght/2, depth -1)
            backward(lenght)
            left(120)


sierpinski(600,7)

speed(10000)
color('white')
penup()
goto(1000,1000)


for i in range(0,500):
    forward(i)
    left(45)
turtles.done()

