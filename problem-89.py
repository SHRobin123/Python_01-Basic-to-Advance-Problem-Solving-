#Insertion Sort

nums = [5, 2, 9, 1, 7]

for i in range(1, len(nums)):
    key = nums[i]
    j = i - 1

    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]
        j = j - 1

    nums[j + 1] = key

print("Sorted List:", nums)

'''
output:-

Sorted List: [1, 2, 5, 7, 9]
'''