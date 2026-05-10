#Sum of N Numbers
n = int(input("Enter a number: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Total Sum =", sum)

'''
Enter a number: 5
Total Sum = 15
'''