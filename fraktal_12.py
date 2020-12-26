import turtle
import  random


def make_fractal(length, langle, rangle, iterations, axiom, target, replace, target2, replace2):
    state = axiom
    turtle.speed(0)
    broj = random.randint(-3, 5)
    ugao = random.randint(-360, 360)
    # make the L-System we want to process
    for i in range(iterations):
        nextState = ''
        for character in state:
            if character == target:
                nextState += replace
            elif character == target2:
                nextState += replace2
            else:
                nextState += character
        state = nextState

    turtle.down()  # pen down
    turtle.color('red', 'black')  # draw line in red, fill black
    turtle.begin_fill()  # set the fill setting

    for move in state:  # another way to loop through all the characters in a string
        if move == "F":
            turtle.left(6787)
            turtle.backward(i)
            turtle.right(90)
            turtle.left(ugao)
            turtle.forward(-3)
            turtle.dot(5, "blue")
            turtle.circle(i, 50, 2)
            turtle.forward(broj)
            turtle.forward(length)
        elif move == "L":
            turtle.left(langle)
        elif move == "R":
            turtle.right(rangle)


if __name__ == '__main__':
    iterations = int(input("Enter the number of generations: "))
    myLen = int(input("Enter the forward movement length: "))

    # JP curve drawing
    make_fractal(myLen, 90, 90, iterations, 'FX', 'X', 'XRYFR', 'Y', 'LFXLY')

turtle.penup()
turtle.goto(6000, 6000)

for i in range(0, 1550):
    turtle.forward(i)
    turtle.left(45)
