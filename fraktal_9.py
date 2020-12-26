from turtle import *
screensize(5000,4000, 'black')
color = ("gainsboro", "light gray", "silver", "dark gray", "gray", "dim gray", "white smoke")
speed(0)
def ciklus():
    for i in range(1500):
        pencolor(color[i%7])
        forward(i/2)
        left(6787)
        backward(i)
        right(90)
        left(189)
        forward(-3)
        dot(5, "blue")
        circle(i,50,2)
        forward(1)
        left(2)
        backward(5)
        backward(i*3)
        right(70)
        left(129)
        forward(-3)
        forward(i / 2)
        print(i)



        dot(5, "red")
ciklus()

#for i in range(100):
    #penup()
  #  goto(100,-150)
  #  pendown()
   #  pencolor(color[i % 7])
   # forward(i / 2)
    #left(4)
   # backward(i)
   # right(55)
   # dot(2, "red")









penup()
goto(6000,6000)


for i in range(0,1550):
    forward(i)
    left(45)
