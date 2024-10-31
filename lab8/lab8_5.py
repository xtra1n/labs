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

min_value = matrix[-1][-1]
max_value = matrix[0][1]

for i in range(width):
    for j in range(width):
        if i < j and max_value < matrix[i][j]:
            max_value = matrix[i][j]
        if i + j >= width and min_value > matrix[i][j]:
            min_value = matrix[i][j]

print(max_value, min_value)
