#Spiral Matrix Print

def spiral_print(matrix):
    result = []

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:

        # Left to Right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Top to Bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Right to Left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Bottom to Top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = spiral_print(matrix)

print("Spiral Order:", result)

'''
output:- 

Spiral Order: [1, 2, 3, 6, 9, 8, 7, 4, 5]
'''