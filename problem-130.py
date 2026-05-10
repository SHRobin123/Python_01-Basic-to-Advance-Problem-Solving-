#Tuple to List

numbers_tuple = (1, 2, 3, 4, 5)

numbers_list = list(numbers_tuple)

print("Tuple:", numbers_tuple)
print("List:", numbers_list)

# Now we can modify list
numbers_list.append(6)

print("Updated List:", numbers_list)

'''
output:-

Tuple: (1, 2, 3, 4, 5)
List: [1, 2, 3, 4, 5]
Updated List: [1, 2, 3, 4, 5, 6]
'''