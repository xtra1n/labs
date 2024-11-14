# Леонтьев Андрей ИУ7-14Б
# 3. Даны две матрицы A и B, в которых количество столбцов одинаково.
# Подсчитать для каждого столбца матрицы А количество элементов, больших
# среднего арифметического элементов соответствующего столбца матрицы В.
# Вывести полученные значения. Затем преобразовать матрицу В путем
# умножения всех элементов столбца матрицы на посчитанное для этого столбца
# значение, если оно ненулевое. Вывести преобразованную матрицу в виде
# матрицы.


print('Ввод матриц оканчивается пустой строкой')

matrix_A = [list(map(int, input('Введите 1-ю строку матрицы A: ').split()))]

width = len(matrix_A[0])
index = 0

# Ввод матрицы A
while matrix_A[index] != []:
    index += 1
    line = list(map(int, input(
        f'Введите {index+1}-ю строку матрицы A: ').split()))
    if line == []:
        break
    matrix_A.append(line)
    while len(matrix_A[index]) != width and matrix_A[index] != []:
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
index = 0

# Ввод матрицы B
while matrix_B[index] != []:
    while len(matrix_B[index]) != width:
        print('Количество столбцов должно совпадать с матрицей А')
        matrix_B[index] = (list(map(int, input(
            f'Введите {index+1}-ю строку матрицы B: ').split())))
        line = matrix_B[index]
    index += 1
    line = list(map(int, input(
        f'Введите {index+1}-ю строку матрицы B: ').split()))
    if line == []:
        break
    matrix_B.append(line)

print("Исходная матрица B")
for line in matrix_B:
    for i in range(len(line)):
        print("{:<6d}".format(line[i]), end=' ')
    print()


arr_average_B = []
length_B = len(matrix_B)

# Вычисления
print('Количество элементов больше среднеаревметического B:', end ='')
for j in range(width):
    average_B = 0
    for i in range(len(matrix_B)):
        average_B += matrix_B[i][j]
    average_B /= length_B
    cnt = 0
    for i in range(len(matrix_A)):
        if matrix_A[i][j] > average_B:
            cnt += 1
    print(cnt, end=' ')
    if cnt != 0:
        for i in range(len(matrix_B)):
            matrix_B[i][j] *= cnt

print('Измененная матрица:')
for line in matrix_B:
    for i in range(len(line)):
        print("{:<6d}".format(line[i]), end=' ')
    print()
