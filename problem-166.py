#ATM System

class ATM:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print(amount, "Deposited")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "Withdrawn")
        else:
            print("Insufficient Balance")


# account create
user = ATM("Robin", 1000)

user.check_balance()
user.deposit(500)
user.withdraw(300)
user.check_balance()

'''
output:-

Balance: 1000
500 Deposited
300 Withdrawn
Balance: 1200
'''