#Instance Variable (Object Variable)

class Student:
    def __init__(self, name, age):
        self.name = name   # instance variable
        self.age = age     # instance variable

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

# object 1
s1 = Student("Robin", 22)

# object 2
s2 = Student("Andrew", 21)

s1.show()
s2.show()

'''
output:-

Name: Robin
Age: 22
Name: Andrew
Age: 21
'''