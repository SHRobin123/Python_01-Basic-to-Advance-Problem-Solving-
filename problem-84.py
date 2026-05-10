#Reverse List

nums = [1, 2, 3, 4, 5]

reversed_list = []

for i in range(len(nums)-1, -1, -1):
    reversed_list.append(nums[i])

print("Reversed List:", reversed_list)

'''
output:-

Reversed List: [5, 4, 3, 2, 1]
'''