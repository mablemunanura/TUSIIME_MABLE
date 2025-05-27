class Human:
    def intro(self):
        print("I am a human.")

class Male(Human):
    def intro(self):
        print("I am male.")

class Female(Human):
    def intro(self):
        print("I am female.")

p1 = Human()
p1.intro()

p2 = Male()
p2.intro()

p3 = Female()
p3.intro()