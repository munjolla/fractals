import turtle

def make_fractal(lenght, langle,rangle, iterations, axiom, target, replace, target2, replace2):
    state = axiom
    turtle.speed(0)

    for i in range(iterations):
        next_state = ''
        for character in state:
            if character == target:
                next_state += replace
            elif character == target2:
                next_state += replace2
            else:
                next_state += character

        state = next_state

    turtle.down()
    turtle.color("red", "black")
    turtle.begin_fill()

    for move in state:
        if move == "F":
            turtle.forward(lenght)
        elif move == "L":
            turtle.left(langle)

        elif move == "R":
            turtle.right(rangle)

if __name__ == "__main__":
    iterations = int(input("Unesi broj generacija: "))
    my_len = int(input("Unesi duzinu kretanja fraktala: "))


    make_fractal(my_len,90,90, iterations, 'FX', 'X', 'XRYFR','Y','LFXLY')


turtle.penup()
turtle.goto(6000,6000)


for i in range(0,1550):
    turtle.forward(i)
    turtle.left(45)



