# Simple Calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print("Result:", a + b)

elif op == '-':
    print("Result:", a - b)

elif op == '*':
    print("Result:", a * b)

elif op == '/':
    print("Result:", a / b)

else:
    print("Invalid operator")

'''
output:-

Enter first number: 10
Enter second number: 5
Enter operator (+, -, *, /): +
Result: 15.0
'''