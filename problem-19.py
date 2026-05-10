#Sum of Digits
num = int(input("Enter a number: "))

sum = 0

while num > 0:

    digit = num % 10

    sum = sum + digit

    num = num // 10

print("Sum of Digits =", sum)

'''
output:-
Enter a number: 1234

Sum of Digits = 10
'''