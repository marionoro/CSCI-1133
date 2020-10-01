import turtle
import math

## Creates pie chart of radius 50.
def pieChart(flist):
    l = []
    colors = ['red','blue','green','purple','orange']
    totalangle = 0
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    for i in range(len(flist)):
        l.append(flist[i]/sum(flist))
    for i in range(len(l)):
        angle = l[i] * 6.2832
        turtle.fillcolor(colors[i])
        turtle.begin_fill()
        turtle.goto(50*math.cos(totalangle), 50*math.sin(totalangle))
        beginningangle = int((180*totalangle)/3.1416)
        endingangle = int((180*(angle+totalangle))/3.1416)
        for i in range(beginningangle,endingangle):
            turtle.goto(50*math.cos((3.1416*i)/180), 50*math.sin((3.1416*i)/180))
        turtle.goto(0,0)
        turtle.end_fill()
        totalangle += angle
