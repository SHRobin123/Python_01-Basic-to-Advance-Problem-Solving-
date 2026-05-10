#Inheritance (Parent-Child)

class Parent:
    def show_parent(self):
        print("I am Parent class")

class Child(Parent):
    def show_child(self):
        print("I am Child class")

# object create
c1 = Child()

c1.show_parent()
c1.show_child()

'''
output:-

I am Parent class
I am Child class
'''