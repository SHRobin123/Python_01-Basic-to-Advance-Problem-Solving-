#Move Zeros to End

def move_zeros(arr):
    non_zero_index = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1

    for i in range(non_zero_index, len(arr)):
        arr[i] = 0

    return arr


arr = [0, 1, 0, 3, 12]

result = move_zeros(arr)

print("After Moving Zeros:", result)

'''
output:- 

After Moving Zeros: [1, 3, 12, 0, 0]
'''