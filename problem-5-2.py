#Three Numbers Largest

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest number is:", a)

elif b > a and b > c:
    print("Largest number is:", b)

else:
    print("Largest number is:", c)



'''
output :-
Enter first number: 6
Enter second number: 5
Enter third number: 2
Largest number is: 6
'''