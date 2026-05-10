# Compound Interest

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

amount = principal * (1 + rate / 100) ** time

compound_interest = amount - principal

print("Compound Interest:", compound_interest)

'''
output:-

Enter principal amount: 1000
Enter rate: 10
Enter time: 2
Compound Interest: 210.0
'''