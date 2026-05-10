#Count Even Odd

def count_even_odd(arr):
    even = 0
    odd = 0

    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


arr = [1, 2, 3, 4, 5, 6, 7]

even_count, odd_count = count_even_odd(arr)

print("Even Count:", even_count)
print("Odd Count:", odd_count)

'''
output:- 

Even Count: 3
Odd Count: 4
'''