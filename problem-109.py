#Kadane Algorithm (Maximum Subarray Sum)

def kadane(arr):
    max_current = arr[0]
    max_global = arr[0]

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])

        if max_current > max_global:
            max_global = max_current

    return max_global


arr = [-2, -3, 4, -1, -2, 1, 5, -3]

result = kadane(arr)

print("Maximum Subarray Sum:", result)

'''
output:- 

Maximum Subarray Sum: 7
'''