#Fibonacci Series

n = int(input("How many terms: "))

a = 0
b = 1

for i in range(n):

    print(a, end=" ")

    c = a + b

    a = b
    b = c

    '''
    output:-
    How many terms: 10

0 1 1 2 3 5 8 13 21 34

    '''