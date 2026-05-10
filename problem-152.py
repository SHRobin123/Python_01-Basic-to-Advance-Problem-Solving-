#Multiple Inheritance

class Father:
    def show_father(self):
        print("I am Father")

class Mother:
    def show_mother(self):
        print("I am Mother")

class Child(Father, Mother):
    def show_child(self):
        print("I am Child")

# object create
c1 = Child()

c1.show_father()
c1.show_mother()
c1.show_child()

'''
output:-

I am Father
I am Mother
I am Child
'''