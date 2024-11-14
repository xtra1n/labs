# Леонтьев Андрей ИУ7-14Б
# 2. Повернуть квадратную целочисленную матрицу на 90 градусов по часовой
# стрелке, затем на 90 градусов против часовой стрелки. Вывести исходную,
# промежуточную и итоговую матрицы. Дополнительных матриц и массивов не
# вводить. Транспонирование не применять.


matrix = [list(map(int, input('Введите 1-ю строку матрицы: ').split()))]

width = len(matrix[0])

# Ввод матрицы
for index in range(1, width):
    line = list(map(int, input(
        f'Введите {index+1}-ю строку матрицы: ').split()))
    if line == []:
        break
    matrix.append(line)
    while len(matrix[index]) != width and matrix[index] != []:
        print('Количество элементов должно быть таким же как в первой строке')
        matrix[index] = (list(map(int, input(
            f'Введите в {index+1}-ю строку матрицы: ').split())))
        line = matrix[index]

print("Исходная матрица")
for line in matrix:
    for i in range(len(line)):
        print("{:<6d}".format(line[i]), end=' ')
    print()

for i in range(width // 2):
    for j in range(i, width - i - 1):
        temp = matrix[i][j]
        matrix[i][j] = matrix[width - j - 1][i]
        matrix[width - j - 1][i] = matrix[width - i - 1][width - j - 1]
        matrix[width - i - 1][width - j - 1] = matrix[j][width - i - 1]
        matrix[j][width - i - 1] = temp

print('Измененная матрица (1):')
for line in matrix:
    for i in range(len(line)):
        print("{:<6d}".format(line[i]), end=' ')
    print()

for i in range(width // 2 + int(width % 2 != 0)):
    for j in range(width - i):
        matrix[i][j], matrix[width - i - 1][width - j - 1] = matrix[width - i - 1][width - j - 1], matrix[i][j]
print('Измененная матрица (2):')

for line in matrix:
    for i in range(len(line)):
        print("{:<6d}".format(line[i]), end=' ')
    print()


