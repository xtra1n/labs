# 4. Наименьшее количество чётных элементов.

print('Ввод матрицы должен оканчиваться пустой строкой ')

matrix = [list(map(str, input('Введите 1-ю строку матрицы: ').split()))]

width = len(matrix[0])
index = 0
cnt = 0
line = matrix[0]
max_cnt = -1
min_cnt = width + 1

while matrix[index] != []:
    for i in range(width):
        if int(line[i]) < 0:
            cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
        max_line = index
    if min_cnt >= cnt:
        min_cnt = cnt
        min_line = index
    cnt = 0
    
    index += 1
    line = list(map(str, input(f'Введите {index+1}-ю строку матрицы: ').split()))
    if line == []:
        break
    matrix.append(line)
    while len(matrix[index]) != width and matrix[index] != []:
        print('Количество элементов должно быть таким же как в первой строке')
        matrix[index] = (list(map(str, input(f'Введите в {index+1}-ю строку матрицы: ').split())))
        line = matrix[index] 
print('Изначальная матрица:')
for line in matrix:
    print(*line)

print('\n Измененная матрица:')
matrix[max_line], matrix[min_line] = matrix[min_line], matrix[max_line]

for line in matrix:
    print(*line)