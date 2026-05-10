#Matrix Multiplication

def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

result = matrix_multiply(A, B)

print("Matrix Multiplication:")
for row in result:
    print(row)

'''
output:- 

Matrix Multiplication:
[19, 22]
[43, 50]
'''