# Леонтьев Андрей ИУ7-14Б
# 4. Задана матрица D и массив I, содержащий номера строк, для которых
# необходимо определить максимальный элемент. Значения максимальных
# элементов запомнить в массиве R. Определить среднее арифметическое
# вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
# среднее арифметическое значение.


matrix = [list(map(int, input('Введите 1-ю строку матрицы A: ').split()))]

width = len(matrix[0])
index = 0

# Ввод матрицы
while matrix[index] != []:
    index += 1
    line = list(map(int, input(
        f'Введите {index+1}-ю строку матрицы A: ').split()))
    if line == []:
        break
    matrix.append(line)
    while len(matrix[index]) != width and matrix[index] != []:
        print('Количество элементов должно быть таким же как в первой строке')
        matrix[index] = (list(map(int, input(
            f'Введите в {index+1}-ю строку матрицы A: ').split())))
        line = matrix[index]

print("Исходная матрица")
for line in matrix:
    for i in range(len(line)):
        print("{:<6d}".format(line[i]), end=' ')
    print()

arr_I = []
index = 1
arr_I.append((input(f'Введите {index}-й элемент списка I: ')))

while arr_I[-1] != '':
    arr_I.append((input(f'Введите {index}-й элемент списка I: ')))
    if arr_I[-1] != '' and int(arr_I[-1]) > len(matrix):
        print('Номер строки превышает количество строк матрицы')
        arr_I[-1] = (input(f'Введите {index}-й элемент списка I: '))

if arr_I != []:
    arr_R = []

    for i in arr_I[:-1]:
        i = int(i)
        max_elem = matrix[i][0]
        for j in range(width):
            if max_elem < matrix[i][j]:
                max_elem = matrix[i][j]
        arr_R.append(max_elem)

    average_R = sum(arr_R) / len(arr_R)

    for line in matrix:
        print(*line)
    
print('Массив I: ', *arr_I)
print('Массив R: ', *arr_R)
print('Среднее арефметическое: ', average_R)
