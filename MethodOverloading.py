class A:
    def intro(self):
        print("I am super class A")

class B(A):
    def intro(self, int):
        print("I am child class B and I take in an int.")
        print(int)

class C(A):
    def intro(self, float):
        print("I am child class C and I take in a float.")
        print(float)

p1 = A()
p1.intro()

p2 = B()
p2.intro(3)

p3 = C()
p3.intro(5.0)

#Real-life Example
import math
class Shape:
    def area(self):
        print("Calculating Area...")

class Square(Shape):
    def area(self, side):
        print(f"Area of the square: {side **2}")

class Rectangle(Shape):
    def area(self, length, width):
        print(f"Area of the rectangle: {length * width}")

s = Square()
s.area(6)

r = Rectangle()
r.area(5,4)