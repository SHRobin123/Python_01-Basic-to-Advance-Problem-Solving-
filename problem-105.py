#List Comprehension Problems

#Example 1: Square of numbers
arr = [1, 2, 3, 4, 5]
squares = [x * x for x in arr]

print("Squares:", squares)

#Example 2: Even numbers only
evens = [x for x in arr if x % 2 == 0]

print("Even Numbers:", evens)

#Example 3: Multiply by 2
double = [x * 2 for x in arr]

print("Doubled:", double)

'''
output:- 

Squares: [1, 4, 9, 16, 25]
Even Numbers: [2, 4]
Doubled: [2, 4, 6, 8, 10]
'''