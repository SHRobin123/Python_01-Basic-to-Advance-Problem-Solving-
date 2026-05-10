#Password Hashing Example

import hashlib

# user password
password = input("Enter password: ")

# create hash object
hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("Original Password:", password)
print("Hashed Password:", hashed_password)

'''
output:-

Enter password: 12345

Original Password: 12345
Hashed Password: 5994471abb01112afcc18159f6cc74b4f511b99806...
'''