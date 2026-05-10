#Multilevel Inheritance (Chain)

class GrandParent:
    def show_grandparent(self):
        print("I am GrandParent")

class Parent(GrandParent):
    def show_parent(self):
        print("I am Parent")

class Child(Parent):
    def show_child(self):
        print("I am Child")

# object create
c1 = Child()

c1.show_grandparent()
c1.show_parent()
c1.show_child()

'''
output:-

I am GrandParent
I am Parent
I am Child
'''