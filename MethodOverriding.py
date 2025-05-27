class A:
    def intro(self):
        print("I am super class A.")

class B(A):
    def intro(self):
        print("I am child class B.")

class C(A):
    def intro(self):
        print("I am child class C.")

p1 = A()
p1.intro()

p2 = B()
p2.intro()

p3 = C()
p3.intro()

#Real-life Example
import math
class Shape:
    def area(self):
        print("Calculating Area...")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of the circle: {math.pi * self.radius **2: .2f}")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print(f"Area of the square: {self.side **2}")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Area of the rectangle: {self.length * self.width}")

c = Circle(2)
c.area()

s = Square(4)
s.area()

r = Rectangle(4,3)
r.area()