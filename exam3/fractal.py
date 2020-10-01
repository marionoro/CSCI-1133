# Paul Opheim ophei033

# I understand that this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing any aspect of the exam
# with anyone is academic misconduct and will result in failing the course.
# I further certify that this program represents my own own work and that none of
# it was obtained from any source other than material presented as part of the
# course.

import turtle
from complex import Complex
from mandelbrot import Mandelbrot

# Creates the Display class which generates a 2x2 visualization of the Mandelbrot set.
class Display:
    def __init__(self):
        self.myt = turtle.Turtle()
        self.myscr = self.myt.getscreen()
        self.myscr.tracer(5000,0)
        self.myscr.listen()
        self.myscr.onclick(self.click)
        self.myt.hideturtle()
        self.myt.speed(0)
        self.myt.pensize(1)
        self.myt.penup()
        self.bounds = [-2, -2, 2, 2]
        self.myt.goto(-300, -300)
        self.draw()
    def click(self, x, y):
        if self.myt.pos() == (300, 300) and x in range(-300,300) and y in range(-300, 300):
            self.zoom(x, y)
    def zoom(self, x, y):
        newwidth = 0.5 * (self.bounds[2] - self.bounds[0])
        newheight = 0.5 * (self.bounds[3] - self.bounds[1])
        newhalfwidth = 0.5 * newwidth
        newhalfheight = 0.5 * newheight
        realpoint = (x * newwidth / 300) + (self.bounds[0] + newwidth)
        imagpoint = (y * newheight / 300) + (self.bounds[1] + newheight)
        if (realpoint - newhalfwidth) < -2:
            self.bounds[0] = -2
            self.bounds[2] = -2 + newwidth
        elif (realpoint + newhalfwidth) > 2:
            self.bounds[2] = 2
            self.bounds[0] = 2 - newwidth
        else:
            self.bounds[0] = realpoint - newhalfwidth
            self.bounds[2] = realpoint + newhalfwidth
        if (imagpoint - newhalfheight) < -2:
            self.bounds[1] = -2
            self.bounds[3] = -2 + newheight
        elif (imagpoint + newhalfheight) > 2:
            self.bounds[3] = 2
            self.bounds[1] = 2 - newheight
        else:
            self.bounds[1] = imagpoint - newhalfwidth
            self.bounds[3] = imagpoint + newhalfwidth
        self.draw()
    def draw(self):
        self.myt.clear()
        halfwidth = 0.5 * (self.bounds[2] - self.bounds[0])
        halfheight = 0.5 * (self.bounds[3] - self.bounds[1])
        self.myt.goto(-300, -300)
        for x in range(-300, 301):
            realpoint = (x * halfwidth / 300) + (self.bounds[0] + halfwidth)
            self.myt.goto(x, -300)
            self.myt.pendown()
            for y in range(-300, 301):
                self.myt.goto(x,y)
                imagpoint = (y * halfheight / 300) + (self.bounds[1] + halfheight)
                color = Mandelbrot(Complex(realpoint, imagpoint)).get_color()
                self.myt.color(color)
            self.myt.penup()

def main():
    Display()

if __name__ == '__main__':
    main()
