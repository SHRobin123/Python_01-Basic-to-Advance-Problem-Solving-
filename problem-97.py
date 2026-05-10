#Pair With Given Sum

def has_pair_with_sum(arr, target):
    seen = set()

    for num in arr:
        if target - num in seen:
            return True
        seen.add(num)

    return False


arr = [1, 4, 7, 2, 5]
target = 9

result = has_pair_with_sum(arr, target)

print("Pair Exists:", result)

'''
output:- 

Pair Exists: True
'''