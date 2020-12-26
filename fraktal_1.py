from turtle import *
import random
speed(0)
pencolor("black")
fillcolor("gray")
begin_fill()
penup()
screensize(5000,4000, "white")
goto(0,-100)
pendown()
broj_forward= random.randint(-3,5)
def poligon(sides, side_len):


    for i in range(0,sides):
        forward(side_len)
        left(300/sides/2.4)
    if side_len >-200:
        left(3)

        forward(broj_forward)
        poligon(sides, side_len-2)

poligon(4,200)
end_fill()


color('white')
penup()
goto(1000,1000)


for i in range(0,350):
    forward(i)
    left(45)
