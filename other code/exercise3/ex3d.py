import turtle
import math
turtle.showturtle()
turtle.setworldcoordinates(-400, -400, 400, 400)

def draw_centercircle(earth):
    earth.goto(40, 0)
    earth.fillcolor("red")
    earth.begin_fill()
    for i in range(0, 360):
        earth.goto(40 * math.cos((i*6.284)/360), 40 * math.sin((i*6.284)/360))
    earth.end_fill()

def main():
    earth = turtle.Turtle()
    moon = turtle.Turtle()
    earth.speed(4)
    moon.speed(20l)
    earth.penup()
    draw_centercircle(earth)
    earth.penup()
    moon.penup()
    earth.goto(150, 0)
    moon.goto(230, 0)
    earth.shape("circle")
    earth.color("green")
    moon.shape("circle")
    moon.color("gray")
    a = 0
    while a < 541:
        earth.goto(150 * math.cos((a*12.568)/360), 150 * math.sin((a*12.568)/360))
        x = earth.pos()[0]
        y = earth.pos()[1]
        b=0
        while b < 73:
            moon.goto(x + (80 * math.cos((b*31.416)/360)), y + (80 * math.sin((b*31.416)/360)))
            b += 1
        a += 1

if __name__ == '__main__':
    main()
