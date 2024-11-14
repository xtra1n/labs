# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №8 “Матрицы. Часть 1”
# 4. Переставить местами столбцы с максимальной и минимальной суммой элементов.

print('Ввод матрицы должен оканчиваться пустой строкой ')

# Запрашиваем первую строку матрицы
matrix = [list(map(int, input('Введите 1-ю строку матрицы: ').split()))]

width = len(matrix[0])
index = 0
coloumn_sum = 0
max_sum, max_coloumn = 0, 0
min_sum, min_coloumn = 0, 0
line = matrix[0]


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


print("Исходная матрица")
for line in matrix:
    for i in range(len(line)):
        print("{:<6d}".format(line[i]), end='')
    print()
    
for line in matrix:
    max_sum += line[0]
    min_sum += line[0]

# Делаем обход по столбцам и запоминаем по необходимым кретериям
for j in range(width):
    if max_sum is None or coloumn_sum > max_sum:
        max_sum = coloumn_sum
        max_coloumn = j
    if min_sum is None or coloumn_sum < min_sum:
        min_sum = coloumn_sum
        min_coloumn = j
    coloumn_sum = 0
    for i in range(1, (len(matrix))):
        coloumn_sum += matrix[i][j]

# Проходимся по матрице, меняем местами найденные стобцы и выводим
print('Измененная матрица:')
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if j == max_coloumn:
            matrix[i][j], matrix[i][min_coloumn] = matrix[i][min_coloumn], matrix[i][j]
    print("".join(f"{elem:<6d}" for elem in matrix[i]))
