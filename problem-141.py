#Recursive Binary Search
def binary(arr, low, high, x):
    if low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary(arr, low, mid-1, x)
        else:
            return binary(arr, mid+1, high, x)
    return -1

arr = [1,2,3,4,5]
print(binary(arr, 0, 4, 3))

'''
output:- 

2
'''