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