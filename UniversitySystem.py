class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self,name, age, regno, course):
        super().__init__(name, age)
        self.regno = regno
        self.course = course

    def print_details(self):
        super().print_details()
        print(f"RegNo: {self.regno}")
        print(f"Course: {self.course}")
        print("\n")

class Lecturer(Person):
    def __init__(self,name, age, id, college):
        super().__init__(name, age)
        self.id = id
        self.college = college

    def print_details(self):
        super().print_details()
        print(f"ID: {self.id}")
        print(f"College: {self.college}")
        print("\n")

class Staff(Person):
    def __init__(self,name, age, role):
        super().__init__(name, age)
        self.role = role

    def print_details(self):
        super().print_details()
        print(f"Role: {self.role}")
        print("\n")

s = Student("Mable", 20, "23/U/1494", "BSSE")
s.print_details()

l = Lecturer("Tusiime", 45, "L002", "CoCIS")
l.print_details()

stf = Staff("Munanura", 37, "Waitress") 
stf.print_details()