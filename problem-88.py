#Selection Sort

nums = [5, 2, 9, 1, 7]

n = len(nums)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if nums[j] < nums[min_index]:
            min_index = j

    nums[i], nums[min_index] = nums[min_index], nums[i]

print("Sorted List:", nums)

'''
output:-

Sorted List: [1, 2, 5, 7, 9]
'''