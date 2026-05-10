#Validate Phone Number
phone = input("Enter phone number: ")

if len(phone) == 11 and phone.isdigit() and phone.startswith("01"):
    result = "Valid Phone Number"
else:
    result = "Invalid Phone Number"

print("Result:", result)

'''
output:-

Enter phone number: 01712345678
Result: Valid Phone Number
'''