#Average of List

nums = [10, 45, 3, 99, 23, 67]

total = 0
count = 0

for i in nums:
    total = total + i
    count = count + 1

average = total / count

print("Average:", average)

'''
output:-

Average: 41.166666666666664
'''