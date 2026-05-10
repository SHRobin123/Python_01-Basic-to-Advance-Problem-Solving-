#Binary Search

nums = [10, 20, 30, 40, 50]
target = 40

left = 0
right = len(nums) - 1

found = False

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        print("Found at index:", mid)
        found = True
        break

    elif nums[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

if not found:
    print("Not Found")

'''
output:-

Found at index: 3
'''