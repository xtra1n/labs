# Леотьев Андрей ИУ7-14Б
# 7. Ввести трёхмерный массив (массив матриц размера x*y*z). Вывести срез
# массива по большему измерению, индекс среза – середина размерности с
# округлением в меньшую сторону.

# Вводим три измерения
x, y, z = list(map(int, input("Введите размер (x,y,z) через пробел: ").split()))
while x < 1 or y < 1 or z < 1:
    x, y, z = list(map(int, input("Введите измерения трёхмерной матрицы через пробел: ").split()))
super_matrix = []
for i in range(x):
    matrix = []
    for j in range(y):
        line = list(map(int, input(f"Введите строку {j + 1} матрицы {i + 1}: ").split()))
        while len(line) != z:
            print(f"Количество элементов должно равняться {z}")
            line = list(map(int, input(f"Введите строку {j + 1} матрицы {i + 1}: ").split()))
        matrix.append(line)
    super_matrix.append(matrix)

# Вычисляем максимальное измерениие
max_meas = -1
if x > y and x > z:
    max_meas = x
elif y > x and y > z:
    max_meas = y
elif z > x and z > y:
    max_meas = z
section = max_meas // 2

# Выводим максимальное измерение
print('Измененная матрица:')
if max_meas == x:
    for i in range(y):
        for j in range(z):
            print(f'{super_matrix[section][i][j]:>6g}', end=' ')
        print()
elif max_meas == y:
    for i in range(x):
        for j in range(z):
            print(f'{super_matrix[i][section][j]:>6g}', end=' ')
        print()
else:
    for i in range(x):
        for j in range(y):
            print(f'{super_matrix[i][j][section]:>6g}', end=' ')
        print()