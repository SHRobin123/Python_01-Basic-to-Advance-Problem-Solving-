#Password Checker

password = input("Enter password: ")

has_digit = False

if len(password) >= 6:
    for ch in password:
        if ch.isdigit():
            has_digit = True
            break

    if has_digit:
        print("Strong Password")
    else:
        print("Weak Password: must contain a number")
else:
    print("Weak Password: too short")

'''
output:-

Enter password: abc12
Weak Password: too short
'''