#Rotate Matrix (90 degree clockwise)

def rotate_matrix(matrix):
    n = len(matrix)

    # Step 1: Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

    return matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = rotate_matrix(matrix)

print("Rotated Matrix:")
for row in result:
    print(row)

'''
output:- 

Rotated Matrix:
[7, 4, 1]
[8, 5, 2]
[9, 6, 3]
'''