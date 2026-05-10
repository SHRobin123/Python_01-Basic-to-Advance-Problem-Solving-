#Bank Management System

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, "Deposited")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "Withdrawn")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Name:", self.name)
        print("Balance:", self.balance)


# account create
b1 = BankAccount("Robin", 1000)

b1.deposit(500)
b1.withdraw(300)
b1.show_balance()

'''
output:-

500 Deposited
300 Withdrawn
Name: Robin
Balance: 1200
'''