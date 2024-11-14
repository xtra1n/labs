# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №8 “Матрицы. Часть 1”
# 5. Найти максимальное значение в квадратной матрице над главной диагональю и минимальное - под побочной диагональю.

matrix = [list(map(int, input('Введите 1-ю строку матрицы: ').split()))]

width = len(matrix[0])
index = 0
line = matrix[0]
column = -1

if len(matrix[0]) > 1:
    # Ввод матрицы
    for index in range(1, width):
        line = list(map(int, input(
            f'Введите {index+1}-ю строку матрицы: ').split()))
        if line == []:
            break
        matrix.append(line)
        while len(matrix[index]) != width:
            print('Количество элементов должно быть таким же как в первой строке')
            matrix[index] = (list(map(int, input(
                f'Введите в {index+1}-ю строку матрицы: ').split())))
            line = matrix[index]

    print("Исходная матрица")
    for line in matrix:
        for i in range(len(line)):
            print("{:<6d}".format(line[i]), end=' ')
        print()

    # Переменные для максимального и минимального
    min_value = matrix[-1][-1]
    max_value = matrix[0][1]

    # Делаем обход и проверяем элементы по условию
    for i in range(width):
        for j in range(width):
            if i < j and max_value < matrix[i][j]:
                max_value = matrix[i][j]
            if i + j >= width and min_value > matrix[i][j]:
                min_value = matrix[i][j]

    print(f'Максимальное значение над главной диагональю: {max_value}\n'
          f'Минимальное значение под побочной диагональю: {min_value}')
else:
    print('Матрица состоит из одного элемента.')
