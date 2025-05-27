class A:
    def method(self):
        print("I am class A")

class B(A):
    def method(self):
        print("I am class B")

class C(A):
    def method(self):
        print("I am class C")

class D(B, C):
    pass

d = D()
d.method()

print(D.mro())