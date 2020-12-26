from turtle import  *
speed(0)
right(30)
shape('triangle')
screensize(5000,4000, "white")
pensize(1)

def sierpinski (lenght, order):
    if order ==0:
        stamp()
    else:
        for i in range(0,3):
            forward(lenght)
            sierpinski(lenght/2, order-1)
            backward(lenght)
            left(120)

sierpinski(250,5)


color('white')
penup()
goto(1000,1000)


for i in range(0,500):
    forward(i)
    left(45)
