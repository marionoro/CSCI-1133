from complex import Complex

# Creates a class which generates the mandelbrot sequence and cardinality at a given starting complex value.
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
