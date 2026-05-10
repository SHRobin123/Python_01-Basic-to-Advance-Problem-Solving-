# Find Maximum of 3 Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    max_num = a
elif b >= a and b >= c:
    max_num = b
else:
    max_num = c

print("Maximum number is:", max_num)

'''
output:-

Enter first number: 10
Enter second number: 25
Enter third number: 15
Maximum number is: 25
'''
