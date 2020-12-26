import turtle

turtle.pencolor("black")
turtle.fillcolor("gray")
turtle.speed(0)
turtle.begin_fill()

for i in range(0,500):
    turtle.forward(i*2)
    turtle.left(140)

turtle.end_fill()





turtle.speed(10000)
turtle.color('white')
turtle.penup()
turtle.goto(1000,1000)


for i in range(0,500):
    turtle.forward(i)
    turtle.left(45)
