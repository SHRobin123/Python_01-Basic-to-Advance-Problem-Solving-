#Matrix Transpose

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)

    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

result = transpose_matrix(matrix)

print("Transpose Matrix:")
for row in result:
    print(row)

'''
output:- 

Transpose Matrix:
[1, 4]
[2, 5]
[3, 6]
'''