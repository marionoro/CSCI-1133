import turtle
import math
turtle.showturtle()
turtle.setworldcoordinates(-200, -200, 200, 200)

def draw_centercircle():
    turtle.goto(40, 0)
    turtle.fillcolor("blue")
    turtle.begin_fill()
    for i in range(0, 360):
        turtle.goto(40 * math.cos((i*6.284)/360), 40 * math.sin((i*6.284)/360))
    turtle.end_fill()

def main():
    turtle.speed(1)
    turtle.penup()
    draw_centercircle()
    turtle.penup()
    turtle.goto(150, 0)
    turtle.shape("circle")
    turtle.color("yellow")
    a = 0
    while a < 1080:
        turtle.goto(150 * math.cos((a*6.284)/360), 150 * math.sin((a*6.284)/360))
        a += 1

if __name__ == '__main__':
    main()
