


def cantor_set(x,y,l):
    if l > 1: #keep doing this while the line is > 1 pixel lon
        win.create_line(x,y,x+l,y) #draw horizontal lin
        y = y + 50 #move 50 pixels down for next generation
        cantor_set(x,y,l/3) #left hand offspring
        cantor_set(x+2/3*l,y,l/3) #right hand offspring

from tkinter import *
w,h = 1500,500
win = Canvas(Tk(),width=w,height=h)
win.pack()
cantor_set(10,10,w-20)
