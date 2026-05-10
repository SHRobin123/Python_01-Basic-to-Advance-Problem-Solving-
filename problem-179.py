# Custom Exception

class AgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise AgeError("Age must be 18 or above!")

    print("You are eligible")

except AgeError as e:
    print("Custom Error:", e)

except ValueError:
    print("Error: Please enter a valid number!")

finally:
    print("Program finished")

'''
output:-

Enter your age: 16
Custom Error: Age must be 18 or above!
Program finished
'''