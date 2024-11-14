# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №8 “Матрицы. Часть 1”
# 2. Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов.


print('Ввод матрицы должен оканчиваться пустой строкой ')

# Запрашиваем первую строку матрицы
matrix = [list(map(int, input('Введите 1-ю строку матрицы: ').split()))]

width = len(matrix[0])  # Запоминаем ширину матрицы
index = 0
cnt = 0
line = matrix[0]
# Вводим переменные для количества отрицательный элементов
max_cnt = -1
min_cnt = width + 1

# Запрашиваем ввод матрицы. пока не будет пустой строки
while matrix[index] != []:
    # Cчитаем количество отрицательных в строке
    for i in range(width):
        if line[i] < 0:
            cnt += 1
    # Запоминаем строку с максимальным и минимальным количеством
    if max_cnt < cnt:
        max_cnt = cnt
        max_line = index
    if min_cnt >= cnt:
        min_cnt = cnt
        min_line = index
    cnt = 0
    index += 1
    # Запрашиваем следующую строку
    line = list(map(int, input(
        f'Введите {index+1}-ю строку матрицы: ').split()))
    if line == []:  # Если введена пустая строка, завершаем цикл
        break
    matrix.append(line)
    # Проверяем корректность введенной строки
    while len(matrix[index]) != width and matrix[index] != []:
        print('Количество элементов должно быть таким же как в первой строке')
        matrix[index] = (list(map(int, input(
            f'Введите в {index+1}-ю строку матрицы: ').split())))
        line = matrix[index]

if len(matrix) > 1:
    print("Исходная матрица")
    for line in matrix:
        for i in range(len(line)):
            print("{:<6d}".format(line[i]), end=' ')
        print()

    # Меняем местами строки
    matrix[max_line], matrix[min_line] = matrix[min_line], matrix[max_line]
    print('\nИзмененная матрица:')
    for line in matrix:
        for i in range(len(line)):
            print("{:<6d}".format(line[i]), end=' ')
        print()
else:
    print('Задана пустая матрица')