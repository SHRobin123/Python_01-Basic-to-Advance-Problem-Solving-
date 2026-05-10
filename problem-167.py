#Shape Area System (Polymorphism)

class Shape:
    def area(self):
        print("Calculate Area")

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        print("Circle Area:", 3.1416 * self.r * self.r)

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        print("Rectangle Area:", self.l * self.w)


# objects
c = Circle(5)
r = Rectangle(4, 6)

c.area()
r.area()

'''
output:-

Circle Area: 78.53999999999999
Rectangle Area: 24
'''