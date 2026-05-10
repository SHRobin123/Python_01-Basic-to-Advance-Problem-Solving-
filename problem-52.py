#Anagram Check
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    result = "Anagram"
else:
    result = "Not Anagram"

print("Result:", result)

'''
output:-

Enter first string: listen
Enter second string: silent
Result: Anagram
'''