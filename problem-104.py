#Flatten Nested List

def flatten_list(nested_list):
    result = []

    for item in nested_list:
        if type(item) == list:
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result


arr = [1, [2, 3], [4, [5, 6]], 7]

result = flatten_list(arr)

print("Flatten List:", result)

'''
output:- 

Flatten List: [1, 2, 3, 4, 5, 6, 7]
'''