# Paul Opheim ophei033

# I understand that this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing any aspect of the exam
# with anyone is academic misconduct and will result in failing the course.
# I further certify that this program represents my own own work and that none of
# it was obtained from any source other than material presented as part of the
# course.

# Creates a class for complex numbers.
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
