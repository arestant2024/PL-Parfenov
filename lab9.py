def create_matrix(n):
    return [[j + i * n + 1 for j in range(n)] for i in range(n)]

def divide_kth_row(matrix, k):
    diagonal_element = matrix[k][k]
    for j in range(len(matrix[k])):
        matrix[k][j] /= diagonal_element

n = 4
matrix = create_matrix(n)
print("Исходная матрица:")
for row in matrix:
    print(row)

k = 2

divide_kth_row(matrix, k)

print("Матрица после деления k строки на элемент:")
for row in matrix:
    print(row)







def create_square_matrix(n):
    return [[j + i * n + 1 for j in range(n)] for i in range(n)]

def transpose_matrix(matrix):
    n = len(matrix)
    transposed = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transposed[j][i] = matrix[i][j]
    return transposed

n = 4
matrix = create_square_matrix(n)
print("Исходная квадратная матрица:")
for row in matrix:
    print(row)

transposed_matrix = transpose_matrix(matrix)

print("Транспонированная матрица:")
for row in transposed_matrix:
    print(row)