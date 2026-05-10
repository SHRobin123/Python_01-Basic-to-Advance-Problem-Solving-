#JWT Token System Example

import jwt
import datetime

# secret key
SECRET_KEY = "mysecretkey"

# user data
payload = {
    "username": "admin",
    "role": "developer",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
}

# create token
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

print("Generated Token:")
print(token)

# decode token
decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

print("\nDecoded Data:")
print(decoded)

'''
output:-

Generated Token:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

Decoded Data:
{'username': 'admin', 'role': 'developer'}
'''