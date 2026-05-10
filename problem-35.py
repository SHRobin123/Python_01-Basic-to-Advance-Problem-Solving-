#ATM Simulation

balance = 1000  # initial balance

print("Welcome to ATM")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Your balance is:", balance)

elif choice == 2:
    deposit = int(input("Enter deposit amount: "))
    balance += deposit
    print("After deposit, balance is:", balance)

elif choice == 3:
    withdraw = int(input("Enter withdraw amount: "))
    if withdraw <= balance:
        balance -= withdraw
        print("After withdraw, balance is:", balance)
    else:
        print("Insufficient balance!")

else:
    print("Invalid choice")

'''
output:-

Welcome to ATM
1. Check Balance
2. Deposit Money
3. Withdraw Money
Enter your choice: 2
Enter deposit amount: 500
After deposit, balance is: 1500
'''