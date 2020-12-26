from turtle import *
speed(100)

def polygon (sides, lenght):
    for i in range(0, sides):
        forward(lenght)
        left(360/sides)
    if lenght > 1:
        left(3)
        polygon(sides, lenght-1)

polygon(20,100)

