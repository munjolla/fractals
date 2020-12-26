from turtle import *
import random
speed(0)
pencolor("black")
fillcolor("gray")
begin_fill()
broj_forward= random.randint(-3,5)
def poligon(sides, side_len):

    for i in range(0, sides+2):
        forward(side_len)
        left(360/sides)

    if side_len > -200:
        left(2)
        forward(8)
        poligon(sides, side_len-1)



poligon(5,00)
end_fill()


color('white')
penup()
goto(1000,1000)


for i in range(0,350):
    forward(i)
    left(45)
