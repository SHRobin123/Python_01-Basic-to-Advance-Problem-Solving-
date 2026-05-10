#Find Second Smallest

nums = [10, 45, 3, 99, 67]

smallest = nums[0]
second_smallest = float('inf')

for i in nums:
    if i < smallest:
        second_smallest = smallest
        smallest = i
    elif i < second_smallest and i != smallest:
        second_smallest = i

print("Second Smallest:", second_smallest)

'''
output:-

Second Smallest: 10
'''