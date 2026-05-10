#Linear Search

nums = [10, 20, 30, 40, 50]
target = 30

found = False

for i in range(len(nums)):
    if nums[i] == target:
        print("Found at index:", i)
        found = True
        break

if not found:
    print("Not Found")

'''
output:-

Found at index: 2
'''