#Polymorphism (Many Forms)

class Bird:
    def sound(self):
        print("Some bird sound")

class Crow(Bird):
    def sound(self):
        print("Crow caws")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")

# object create
b1 = Crow()
b2 = Sparrow()

b1.sound()
b2.sound()

'''
output:-

Crow caws
Sparrow chirps
'''