#Find GCD — Greatest Common Divisor

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1

for i in range(1, min(a, b) + 1):

    if a % i == 0 and b % i == 0:

        gcd = i

print("GCD =", gcd)

#Optimized Method — Euclidean Algorithm

#Formula
#gcd(a,b)=gcd(b,amodb)

'''
a = int(input())
b = int(input())

while b != 0:

    temp = b

    b = a % b

    a = temp

print("GCD =", a)
'''

'''
output:-
Enter first number: 12
Enter second number: 18

GCD = 6
'''