#Three Numbers Smallest

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b and a < c:
    print("Smallest number is:", a)

elif b < a and b < c:
    print("Smallest number is:", b)

else:
    print("Smallest number is:", c)

    ''' 
    output:-

    Enter first number: 50
Enter second number: 12
Enter third number: 30

Smallest number is: 12

    '''