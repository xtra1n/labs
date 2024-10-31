# 4. Наименьшее количество чётных элементов.

print('Ввод матрицы должен оканчиваться пустой строкой ')

matrix = [list(map(str, input('Введите 1-ю строку матрицы: ').split()))]

width = len(matrix[0])
i = 0
cnt = 0
line = matrix[0]
max_line = []

while matrix[i] != []:
    for el in line:
        if int(el) % 2 == 0:
            cnt += 1
    if cnt >= len(max_line) and cnt != 0:
        max_line = line
    cnt = 0
    i += 1
    line = list(map(str, input(f'Введите {i+1}-ю строку матрицы: ').split()))
    if line == []:
        break
    matrix.append(line)
    while len(matrix[i]) != width and matrix[i] != []:
        print('Количество элементов должно быть таким же как в первой строке')
        matrix[i] = (list(map(str, input(
            f'Введите в {i+1}-ю строку матрицы: ').split())))
        line = matrix[i]

print('Изначальная матрица: ')
for line in matrix:
    print(*line)

if max_line != []:
    print('Строка с наименьшим количеством четных', *max_line)
else:
    print('Не нашлось таких элементов')
