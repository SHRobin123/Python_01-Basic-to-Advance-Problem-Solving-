#Matrix Addition

def matrix_addition(A, B):
    rows = len(A)
    cols = len(A[0])

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] + B[i][j])
        result.append(row)

    return result


A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9],
    [1, 2, 3]
]

result = matrix_addition(A, B)

print("Matrix Sum:")
for row in result:
    print(row)

'''
output:- 

Matrix Sum:
[8, 10, 12]
[5, 7, 9]
'''