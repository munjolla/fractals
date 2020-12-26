import turtle
import math
turtle.speed(0)
#turtle.pencolor("black")
#turtle.fillcolor("gray")

def fractal(aturt, depth, maxdepth):
    if depth > maxdepth:
        return
    turtle.begin_fill()
    length = 900 * ((math.sqrt(2) / 2) ** depth)
    anotherturt = aturt.clone()
    aturt.forward(length)
    aturt.left(45)
    fractal(aturt, depth + 1, maxdepth)
    anotherturt.right(90)
    anotherturt.forward(length)
    anotherturt.left(90)
    anotherturt.forward(length)
    if depth != maxdepth:
        turt3 = anotherturt.clone()
        turt3.left(45)
        turt3.forward(180 * ((math.sqrt(2) / 2) ** (1 + depth)))
        turt3.right(90)
        fractal(turt3, depth + 1, maxdepth)
    anotherturt.left(90)
    anotherturt.forward(length)


def draw_fractal():
    window = turtle.Screen()
    turt = turtle.Turtle()
    turt.hideturtle()
    turt.penup()
    turt.goto(-75, -225)
    turt.pendown()
    turt.speed(0)
    turt.left(90)
    fractal(turt, 4, 14)
    window.exitonclick()


draw_fractal()
#turtle.end_fill()