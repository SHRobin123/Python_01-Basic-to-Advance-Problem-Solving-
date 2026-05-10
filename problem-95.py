#Two Sum Problem

def two_sum(arr, target):
    seen = {}

    for i in range(len(arr)):
        diff = target - arr[i]

        if diff in seen:
            return [seen[diff], i]

        seen[arr[i]] = i

    return []


arr = [2, 7, 11, 15]
target = 9

result = two_sum(arr, target)

print("Indices:", result)

'''
output:- 

Indices: [0, 1]
'''