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