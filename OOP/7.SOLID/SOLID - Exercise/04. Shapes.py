from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side


class Triangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return (self.width * self.height) / 2


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.radius * self.radius * pi


class AreaCalculator:

    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area()

        return total


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)



# ''' MY TESTS '''
# shapes = [Rectangle(2, 3), Square(5), Triangle(4, 6), Circle(2)]
# calculator = AreaCalculator(shapes)
# print("The \"ALL\" shapes total area is: ", calculator.total_area)
