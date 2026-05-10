#Find Second Largest

nums = [10, 45, 3, 99, 67]

largest = nums[0]
second_largest = -1

for i in nums:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print("Second Largest:", second_largest)

'''
output:-

Second Largest: 67
'''