#Employee Management System

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print("Name:", self.name, "| Salary:", self.salary)


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, salary):
        e = Employee(name, salary)
        self.employees.append(e)

    def show_all(self):
        print("Employee List:")
        for e in self.employees:
            e.show()


# system create
c = Company()

c.add_employee("Robin", 50000)
c.add_employee("Andrew", 60000)

c.show_all()

'''
output:-

Employee List:
Name: Robin | Salary: 50000
Name: Andrew | Salary: 60000
'''