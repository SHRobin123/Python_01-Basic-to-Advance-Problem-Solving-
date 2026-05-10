#Find Smallest in List

nums = [10, 45, 3, 99, 23, 67]

smallest = nums[0]

for i in nums:
    if i < smallest:
        smallest = i

print("Smallest Number:", smallest)

'''
output:-

Smallest Number: 3
'''