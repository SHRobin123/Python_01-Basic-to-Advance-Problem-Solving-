#Constructor (__init__)

class Student:
    def __init__(self, name, age):
        print("Constructor is called")
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

# object create
s1 = Student("Robin", 22)

# method call
s1.show()

'''
output:-

Constructor is called
Name: Robin
Age: 22
'''