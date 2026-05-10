#Named Tuple

from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "department"])

student1 = Student("Robin", 22, "CSE")

print("Name:", student1.name)
print("Age:", student1.age)
print("Department:", student1.department)

'''
output:-

Name: Robin
Age: 22
Department: CSE
'''