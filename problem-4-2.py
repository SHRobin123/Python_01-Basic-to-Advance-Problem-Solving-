#Another way of swap taking input

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before Swap:")
print(a, b)

a, b = b, a

print("After Swap:")
print(a, b)


'''
Enter first number: 4
Enter second number: 5
Before Swap:
4 5
After Swap:
5 4
'''