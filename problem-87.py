#Bubble Sort

nums = [5, 2, 9, 1, 7]

n = len(nums)

for i in range(n):
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print("Sorted List:", nums)

'''
output:-

Sorted List: [1, 2, 5, 7, 9]
'''