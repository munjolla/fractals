from turtle import *
speed(0)

pencolor("black")
fillcolor("gray")
goto(0,-100)
begin_fill()
def polygon(sides, side_len):
    goto(0, -100)
    for i in range(0, sides):
        forward(side_len)
        left(180*1.7/sides)

    if side_len > -100:
        left(2)
        forward(8)
        right(7)
        backward(2*side_len )
        polygon(sides, side_len-1)


polygon(4,300)
#end_fill()


speed(10000)
color('white')
penup()
goto(1000,1000)


for i in range(0,500):
    forward(i)
    left(45)