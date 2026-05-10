#Remove Even Numbers

def remove_even_numbers(arr):
    result = []

    for num in arr:
        if num % 2 != 0:
            result.append(num)

    return result


arr = [1, 2, 3, 4, 5, 6, 7]

result = remove_even_numbers(arr)

print("After Removing Even Numbers:", result)

'''
output:- 

After Removing Even Numbers: [1, 3, 5, 7]
'''