# Count Special Characters

text = input("Enter a string: ")

count = 0

for char in text:
    if not char.isalnum() and not char.isspace():
        count += 1

print("Special characters count:", count)

'''
output:-

Enter a string: He@llo#123!
Special characters count: 3
'''