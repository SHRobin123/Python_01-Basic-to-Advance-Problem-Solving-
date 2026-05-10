# Log Errors

import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    logging.error("Division by zero error occurred")
    print("Error: Cannot divide by zero!")

except ValueError:
    logging.error("Invalid input provided")
    print("Error: Please enter valid numbers!")

finally:
    print("Program finished")

'''
output:-

Enter first number: 10
Enter second number: 0
Error: Cannot divide by zero!
Program finished
'''