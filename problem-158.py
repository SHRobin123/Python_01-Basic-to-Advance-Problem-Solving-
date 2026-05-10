#Class Method

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    def show(self):
        print("Name:", self.name)
        print("School:", Student.school)

# objects
s1 = Student("Robin")
s2 = Student("Andrew")

# change class variable using class method
Student.change_school("XYZ School")

s1.show()
s2.show()

'''
output:-

Name: Robin
School: XYZ School
Name: Andrew
School: XYZ School
'''