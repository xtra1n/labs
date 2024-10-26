# 4. Наименьшее количество чётных элементов.

print('Ввод матрицы должен оканчиваться "00" ')

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
    while len(matrix[i]) != l:
        print('Количество элементов должно быть таким же как в первой строке')
        matrix[i] = (list(map(str, input(f'Введите в {i+1}-ю строку матрицы: ').split())))   
    
for line in matrix:
    for el in line:
        if int(el) % 2 == 0:
            cnt += 1
    if cnt >= len(max_line):
        max_line = line
        cnt = 0

if max_line != []:
    print(*max_line)
else:
    print('Не нашлось таких элементов')