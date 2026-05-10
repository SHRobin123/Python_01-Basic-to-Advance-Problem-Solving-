#Operator Overloading (+ customize)

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def show(self):
        print("Value:", self.value)

# objects
n1 = Number(10)
n2 = Number(20)

n3 = n1 + n2   # internally calls __add__

n3.show()

'''
output:-

Value: 30
'''