class Complex:
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag
    def __repr__(self):
        if self.imag == 0:
            return str(self.real)
        elif self.imag > 0:
            return str(self.real) + " + " + str(self.imag) + "i"
        else:
            return str(self.real) + " - " + str(abs(self.imag)) + "i"
    def getReal(self):
        return self.real
    def getImag(self):
        return self.imag
    def changeReal(self, value):
        self.real = value
    def changeImag(self, value):
        self.imag = value
    def __add__(self, complex2):
        return Complex(self.real + complex2.real, self.imag + complex2.imag)
    def __mul__(self, complex2):
        return Complex(self.real * complex2.real - self.imag * complex2.imag, self.imag * complex2.real + self.real * complex2.imag)
    def __abs__(self):
        return ((self.real ** 2) + (self.imag ** 2))**0.5

class Mandelbrot:
    def __init__(self, startvalue, limit = 50):
        self.startvalue = startvalue
        self.limit = limit
        self.colormap = ['violet', 'blue', 'green', 'yellow', 'orange', 'red', 'black']
        self.sequence = []
        a = Complex(0, 0)
        for i in range(limit):
            a = (a*a) + self.startvalue
            if abs(a) > 2:
                break
            self.sequence.append(a)
        self.cardinality = len(self.sequence)
    def get_color(self):
        if self.cardinality == self.limit:
            return self.colormap[6]
        elif self.cardinality in range(0,1):
            return self.colormap[0]
        elif self.cardinality in range(1,11):
            return self.colormap[1]
        elif self.cardinality in range(11,21):
            return self.colormap[2]
        elif self.cardinality in range(21,31):
            return self.colormap[3]
        elif self.cardinality in range(31,41):
            return self.colormap[4]
        else:
            return self.colormap[5]

import turtle

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
