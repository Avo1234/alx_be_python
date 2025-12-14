import math
class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    #def area(self):


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__( length, width)

    def area(self):
        return self.length * self.width

class Circle(Shape):
     def __init__(self, radius):
        # super().__init__( length, width)
        self.radius = radius

     def area(self):
        return math.pi*self.radius**2