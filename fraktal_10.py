from turtle import *
import random
screensize(5000,4000, 'black')
color = ("gainsboro", "light gray", "silver", "dark gray", "gray", "dim gray", "white smoke")
speed(0)
broj= random.randint(-3,5)
ugao = random.randint(-360,360)

def ciklus():
    for i in range(1500):
        pencolor(color[i%7])
        forward(i/2)
        left(6787)
        backward(i)
        right(90)
        left(ugao)
        forward(-3)
        dot(5, "blue")
        circle(i,50,2)
        forward(broj)
        goto(i,i+6)
        left(broj)
        backward(5)
        backward(i*3)

        right(ugao)
        left(ugao)
        right(ugao)
        forward(-3)
        forward(i / 2)
        right(4)
        forward(-3)
        #pencolor("red")
        left(ugao)
        forward(-3)
        forward(i / 2)
        backward(i)
        left(90)
        left(-90)

        forward(1)
        #pencolor("red")
        forward(2*i)
        right(ugao*1.4)
        left(ugao/2.4)
        right(ugao-4)
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