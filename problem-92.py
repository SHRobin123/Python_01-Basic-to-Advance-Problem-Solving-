#Find Missing Number

def find_missing(arr, n):
    total_sum = n * (n + 1) // 2   # formula sum of 1 to n
    array_sum = sum(arr)
    return total_sum - array_sum


arr = [1, 2, 4, 5, 6]
n = 6

missing = find_missing(arr, n)

print("Missing Number:", missing)

'''
output:- 

Missing Number: 3
'''