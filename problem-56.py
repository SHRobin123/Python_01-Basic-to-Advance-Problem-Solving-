#Check Substring
main = input("Enter main string: ")
sub = input("Enter substring: ")

if sub in main:
    result = "Found"
else:
    result = "Not Found"

print("Result:", result)

'''
output:-

Enter main string: hello world
Enter substring: world
Result: Found
'''