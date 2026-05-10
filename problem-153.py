#Method Overriding

class Parent:
    def show(self):
        print("I am Parent class")

class Child(Parent):
    def show(self):
        print("I am Child class (Overridden)")

# object create
c1 = Child()

c1.show()

'''
output:-

I am Child class (Overridden)
'''