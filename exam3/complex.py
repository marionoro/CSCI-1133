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
