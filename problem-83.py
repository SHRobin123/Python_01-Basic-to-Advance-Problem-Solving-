#Rotate List

nums = [1, 2, 3, 4, 5]
k = 2  # কতটা rotate করবে

n = len(nums)

k = k % n  # যদি বড় number দেওয়া হয়

rotated = nums[-k:] + nums[:-k]

print("Rotated List:", rotated)

'''
output:-

Rotated List: [4, 5, 1, 2, 3]
'''