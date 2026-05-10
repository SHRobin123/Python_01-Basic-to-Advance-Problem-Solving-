#Class Variable (Shared Variable)

class Student:
    school = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name     # instance variable

    def show(self):
        print("Name:", self.name)
        print("School:", Student.school)

# objects
s1 = Student("Robin")
s2 = Student("Andrew")

s1.show()
s2.show()

'''
output:-

Name: Robin
School: ABC School
Name: Andrew
School: ABC School
'''