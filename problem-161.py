#Student Management System

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name, "| Age:", self.age)


class StudentSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, age):
        s = Student(name, age)
        self.students.append(s)

    def show_all(self):
        print("All Students:")
        for s in self.students:
            s.show()


# system create
system = StudentSystem()

# add students
system.add_student("Robin", 22)
system.add_student("Andrew", 21)

# show all students
system.show_all()

'''
output:-

All Students:
Name: Robin | Age: 22
Name: Andrew | Age: 21
'''