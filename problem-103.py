#Diagonal Sum

def diagonal_sum(matrix):
    n = len(matrix)

    main_diag = 0
    sec_diag = 0

    for i in range(n):
        main_diag += matrix[i][i]
        sec_diag += matrix[i][n - 1 - i]

    # if odd size matrix, middle element counted twice
    if n % 2 == 1:
        sec_diag -= matrix[n // 2][n // 2]

    return main_diag + sec_diag


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = diagonal_sum(matrix)

print("Diagonal Sum:", result)

'''
output:- 

Diagonal Sum: 25
'''