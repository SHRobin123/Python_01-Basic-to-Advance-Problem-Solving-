#Remove Duplicates

nums = [1, 2, 2, 3, 1, 4, 4, 5]

unique = []

for i in nums:
    if i not in unique:
        unique.append(i)

print("Unique List:", unique)

'''
output:-

Unique List: [1, 2, 3, 4, 5]
'''