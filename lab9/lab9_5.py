# Леонтьв Андрей ИУ7-14Б
# 5. Даны 2 матрицы А и В. Получить матрицу С, равную произведению матриц А и
# В. Вывести все матрицы в виде матриц.


print('Ввод матриц оканчивается пустой строкой')

matrix_A = [list(map(int, input('Введите 1-ю строку матрицы A: ').split()))]

width_A = len(matrix_A[0])
index = 0

# Ввод матрицы A
while matrix_A[index] != []:
    index += 1
    line = list(map(int, input(
        f'Введите {index+1}-ю строку матрицы A: ').split()))
    if line == []:
        break
    matrix_A.append(line)
    while len(matrix_A[index]) != width_A and matrix_A[index] != []:
        print('Количество элементов должно быть таким же как в первой строке')
        matrix_A[index] = (list(map(int, input(
            f'Введите в {index+1}-ю строку матрицы A: ').split())))
        line = matrix_A[index]

print("Исходная матрица А")
for line in matrix_A:
    for i in range(len(line)):
        print("{:<6d}".format(line[i]), end=' ')
    print()

matrix_B = [list(map(int, input('Введите 1-ю строку матрицы B: ').split()))]
width_B = len(matrix_B[0])

# Ввод матрицы B
for index in range(1, width_A):
    while len(matrix_B[index - 1]) != len(matrix_A):
        print('Количество столбцов должно совпадать с матрицей А')
        matrix_B[index - 1] = (list(map(int, input(
            f'Введите {index}-ю строку матрицы B: ').split())))
        line = matrix_B[index - 1]
    line = list(map(int, input(
        f'Введите {index+1}-ю строку матрицы B: ').split()))
    matrix_B.append(line)

print("Исходная матрица B")
for line in matrix_B:
    for i in range(len(line)):
        print("{:<6d}".format(line[i]), end=' ')
    print()

matrix_C = [[0] * len(matrix_A) for _ in range(width_B) ]

# Умножаем
for i in range(len(matrix_A)):
    for j in range(width_B):
        el = 0
        for ind in range(width_A):
            el += matrix_A[i][ind] * matrix_B[ind][j]
        matrix_C[i][j] = el

print('Матрица C:')
for line in matrix_C:
    print(*line)