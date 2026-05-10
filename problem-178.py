# Exception Handling

try:
    # risky code
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid numbers!")

except Exception as e:
    print("Unknown Error:", e)

finally:
    print("Program finished")

'''
output:-

Enter first number: 10
Enter second number: 0
Error: You cannot divide by zero!
Program finished
'''