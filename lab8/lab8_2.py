# 2. Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов.

print('Ввод матрицы должен оканчиваться пустой строкой ')

matrix = [list(map(str, input('Введите 1-ю строку матрицы: ').split()))]

l = len(matrix[0])
i = 0
cnt = 0
max_line = []

while matrix[i] != []:
    i += 1
    el = list(map(str, input(f'Введите {i+1}-ю строку матрицы: ').split()))
    if el == []:
        break
    matrix.append(el)
    while len(matrix[i]) != l and matrix[i] != []:
        print('Количество элементов должно быть таким же как в первой строке')
        matrix[i] = (list(map(str, input(f'Введите в {i+1}-ю строку матрицы: ').split())))  