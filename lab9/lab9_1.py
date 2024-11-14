# Леонтьев Андрей ИУ7-14Б
# Даны два одномерных целочисленных массива A и B. Сформировать матрицу
# M, такую что m_i_j = a_i * b_j
# Определить количество полных квадратов в каждой строке матрицы.Записать
# значения в массив matrix. Напечатать матрицу M в виде матрицы и рядом столбец matrix.


# Ввод данных
A = list(map(int, input("Введите элементы списка через пробел: ").split()))
while not A:
    print('Список не может быть пустым')
    A = list(map(int, input("Введите элементы списка через пробел: ").split()))

B = list(map(int, input("Введите элементы списка через пробел: ").split()))
while not B:
    print('Список не может быть пустым')
    B = list(map(int, input("Введите элементы списка через пробел: ").split()))

# Считаем переменную для форматирования
output_place = 0
for i in range(len(A)):
    if len(str(A[i])) > output_place:
        output_place = len(str(A[i]))
for i in range(len(B)):
    if len(str(B[i])) > output_place:
        output_place = len(str(B[i]))

# Формируем матрицу
matrix = []
arr_S = []
for i in range(len(A)):
    line = []
    count = 0
    for j in range(len(B)):
        el = A[i] * B[j]
        line.append(el)
        if ((el)**0.5) % 1 == 0:
            count += 1
    arr_S.append(count)
    matrix.append(line)

# Вывод
for i, line in enumerate(matrix):
    for elem in line:
        print("{:>{}d}".format(elem, output_place + 2), end=' ')
    print('|| ', arr_S[i],)
