#Encapsulation (Private Data)

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# object create
b1 = BankAccount("Robin", 1000)

b1.deposit(500)

print("Name:", b1.name)
print("Balance:", b1.get_balance())

'''
output:-

Name: Robin
Balance: 1500
'''