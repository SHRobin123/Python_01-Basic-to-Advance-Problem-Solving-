#Prime Numbers in Range
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for num in range(start, end + 1):

    if num > 1:

        is_prime = True

        for i in range(2, num):

            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)


            
'''
output:-
Enter start number: 1
Enter end number: 20

2
3
5
7
11
13
17
19

'''