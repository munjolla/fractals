import turtle



iterations = input("Enter the number of generations: ") #type in a string
iterations = int(iterations) #now it's an integer
startLength=100 #Length of the generation 0 line

#pick the pen up and move cursor to a good starting point
turtle.up()
turtle.setpos(-startLength*3/2,0)
turtle.speed(0)

#Axiom
Dragon = "F" 

#make the L-System we want to process
for i in range(iterations):
    Dragon = Dragon.replace("F","FLFRFRFFLFLFRF")

turtle.down() #pen down
turtle.screensize(5000,4000, 'black')
turtle.color('red','black') #draw line in red, fill black
turtle.begin_fill() #set the fill setting

for move in Dragon: #another way to loop through all the characters in a string
    if move == "F":
        turtle.forward(startLength / (4 ** (iterations - 1)))
    elif move == "L":
        turtle.left(90)
    elif move == "R":
        turtle.right(90)

#turtle.end_fill() #fill any enclosed areas


turtle.penup()
turtle.goto(6000,6000)


for i in range(0,1550):
    turtle.forward(i)
    turtle.left(45)

