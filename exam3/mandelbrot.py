# Paul Opheim ophei033

# I understand that this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing any aspect of the exam
# with anyone is academic misconduct and will result in failing the course.
# I further certify that this program represents my own own work and that none of
# it was obtained from any source other than material presented as part of the
# course.

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
