#Dictionary Comprehension

numbers = [1, 2, 3, 4, 5]

squares = {x: x*x for x in numbers}

print("Square Dictionary:", squares)

'''
output:-

Square Dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''