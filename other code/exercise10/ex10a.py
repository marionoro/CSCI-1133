import math

class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def setRadius(self, r):
        self.radius = r

    def getCircumference(self):
        return 2.0 * math.pi * self.radius

    def getArea(self):
        return math.pi * self.radius ** 2
