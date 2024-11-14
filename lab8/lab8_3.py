# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №8 “Матрицы. Часть 1”
# 3. Найти столбец, имеющий определённое свойство по варианту
# 2. Наименьшее количество отрицательных элементов

print('Ввод матрицы должен оканчиваться пустой строкой ')

# Запрашиваем первую строку матрицы
matrix = [list(map(int, input('Введите 1-ю строку матрицы: ').split()))]

width = len(matrix[0])
index = 0
line = matrix[0]
column = -1  # Вводим переменную для номера стобца

# Делаем ввод матрицы
while matrix[index] != []:
    index += 1
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

if matrix != []:
    print("Исходная матрица")
    for line in matrix:
        for i in range(len(line)):
            print("{:<6d}".format(line[i]), end=' ')
        print()

    # Вводим переменные для количества отрицательных и длину массива
    min_negative, length = len(matrix), len(matrix)

    # Проходимся по столбцам и ищем с минимальным количеством
    for i in range(width):
        count_negative = 0
        for j in range(length):
            if matrix[j][i] < 0:
                count_negative += 1
        if min_negative > count_negative:
            min_negative = count_negative
            column = i

    print('Столбец с наименьшим количеством отрциательных элементов:')
    for line in matrix:
        for j in range(len(line)):
            if j == column:
                print(line[j])
else:
    print('Задана пустая матрциа')
