# Check Rotation String

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Yes, Rotation String")
else:
    print("No, Not Rotation")

'''
output:-

Enter first string: abcd
Enter second string: cdab
Yes, Rotation String
'''