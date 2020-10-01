import turtle
import math

## Determines frequency of each vowel in a string:
def vowelCount(astring):
    acount = 0
    ecount = 0
    icount = 0
    ocount = 0
    ucount = 0
    totalcount = []
    for i in range(len(astring)):
        if astring[i] == 'A' or astring[i] == 'a':
            acount += 1
        elif astring[i] == 'E' or astring[i] == 'e':
            ecount += 1
        elif astring[i] == 'I' or astring[i] == 'i':
            icount += 1
        elif astring[i] == 'O' or astring[i] == 'o':
            ocount += 1
        elif astring[i] == 'U' or astring[i] == 'u':
            ucount += 1
    totalcount = [acount, ecount, icount, ocount, ucount]
    return totalcount

## Draws a circle of radius 200 with no color
def draw_circle():
    turtle.penup()
    turtle.goto(200, 0)
    turtle.pendown()
    for i in range(0, 360):
        turtle.goto(200 * math.cos((i*3.1416)/180), 200 * math.sin((i*3.1416)/180))

## Prints error message in center of window
def no_vowels():
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.write('No vowels in input', align = 'center', font = ("Arial", 14, "normal"))

## Creates pie chart of radius 200.
def pieChart(flist):
    l = []
    colors = ['red','blue','green','purple','orange']
    letters = ['A','E','I','O','U']
    totalangle = 0
    for i in range(len(flist)):
        l.append(flist[i]/sum(flist))
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    for i in range(len(l)):
        letter = letters[i]
        angle = l[i] * 6.2832
        if angle != 0:
            turtle.fillcolor(colors[i])
            turtle.begin_fill()
            turtle.goto(200*math.cos(totalangle), 200*math.sin(totalangle))
            beginningangle = int((180*totalangle)/3.1416)
            endingangle = int((180*(angle+totalangle))/3.1416)
            for i in range(beginningangle,endingangle):
                turtle.goto(200*math.cos((3.1416*i)/180), 200*math.sin((3.1416*i)/180))
            turtle.goto(200*math.cos(totalangle+angle), 200*math.sin(totalangle+angle))
            turtle.goto(0,0)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(150*math.cos(totalangle+(angle/2)), 150*math.sin(totalangle+(angle/2)))
            turtle.write(letter, align = 'center', font = ("Arial", 14, "normal"))
            turtle.goto(0,0)
            turtle.pendown()
            totalangle += angle

def main():
    turtle.hideturtle()
    string = turtle.textinput("Vowel Counter", "Input your string: ")
    vowellist = vowelCount(string)
    if vowellist == [0,0,0,0,0]:
        draw_circle()
        no_vowels()
    else:
        pieChart(vowellist)


if __name__ == '__main__':
    main()
