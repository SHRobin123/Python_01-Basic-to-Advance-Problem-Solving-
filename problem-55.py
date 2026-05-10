#Count Uppercase Lowercase
s = input("Enter string: ")

upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase Count:", upper)
print("Lowercase Count:", lower)

'''
output:-

Enter string: AbCdE
Uppercase Count: 3
Lowercase Count: 2
'''