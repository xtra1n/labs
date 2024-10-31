# 2. Наименьшее количество отрицательных элементов

matrix = [list(map(str, input('Введите 1-ю строку матрицы: ').split()))]

width = len(matrix[0])
index = 0
line = matrix[0]
column = -1

for index in range(1, width):
    line = list(map(str, input(
        f'Введите {index+1}-ю строку матрицы: ').split()))
    if line == []:
        break
    matrix.append(line)
    while len(matrix[index]) != width:
        print('Количество элементов должно быть таким же как в первой строке')
        matrix[index] = (list(map(str, input(
            f'Введите в {index+1}-ю строку матрицы: ').split())))
        line = matrix[index]

print('Изначальная матрица:')
for line in matrix:
    print(*line)

for i in range(width):
    for j in range(i + 1, width):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print('Измененная матрица:')
for line in matrix:
    print(*line)
