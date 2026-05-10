#Authentication System Example

stored_username = "admin"
stored_password = "12345"

username = input("Enter username: ")
password = input("Enter password: ")

if username == stored_username and password == stored_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")

'''
output:-

Enter username: admin
Enter password: 12345
Login Successful
'''