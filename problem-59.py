#Validate Email
email = input("Enter email: ")

if "@" in email and "." in email:
    at_pos = email.index("@")
    dot_pos = email.rindex(".")

    if at_pos > 0 and dot_pos > at_pos + 1 and dot_pos < len(email) - 1:
        result = "Valid Email"
    else:
        result = "Invalid Email"
else:
    result = "Invalid Email"

print("Result:", result)

'''
output:-

Enter email: test@gmail.com
Result: Valid Email
'''