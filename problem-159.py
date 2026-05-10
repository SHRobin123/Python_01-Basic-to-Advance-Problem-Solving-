#Magic Methods (Dunder Methods)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

# object create
s1 = Student("Robin", 22)

print(s1)

'''
output:-

Name: Robin, Age: 22
'''