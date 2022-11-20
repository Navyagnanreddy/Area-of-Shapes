import math

class Shape(object):
    
    def area(self):
    
       pass

class Square(Shape):
    
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    

class Rectangle(Shape):
    """
    Basic rectangle class
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    

class Circle(Shape):
   
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

def main():
    
    square = Square(5)
    print("Square(5)")
    print("  Area: " + str(square.area()))
   
    rect = Rectangle(5, 4)
    print("Rectangle(5, 4)")
    print("  Area: " + str(rect.area()))

    circle = Circle(5)
    print("Circle(5)")
    print("  Area: " + str(circle.area()))
    
if __name__ == '__main__':
    main()