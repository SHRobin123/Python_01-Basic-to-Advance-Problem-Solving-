#Quick Sort

def quick_sort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[-1]
    left = []
    right = []
    middle = []

    for i in nums:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            middle.append(i)

    return quick_sort(left) + middle + quick_sort(right)

nums = [5, 2, 9, 1, 7]

sorted_list = quick_sort(nums)

print("Sorted List:", sorted_list)

'''
output:-

Sorted List: [1, 2, 5, 7, 9]
'''