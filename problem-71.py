#Find Largest in List

nums = [10, 45, 3, 99, 23, 67]

largest = nums[0]

for i in nums:
    if i > largest:
        largest = i

print("Largest Number:", largest)

'''
output:-

Largest Number: 99
'''