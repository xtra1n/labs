matrix = [list(map(int, input('Введите 1-ю строку матрицы: ').split()))]

width = len(matrix[0])

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

sq = 0

for i in range(width):
    for j in range(len(matrix)):
        if i + j < width - 1:
            sq += 1
            matrix[i][j] = 2 ** sq
            
        
for line in matrix:
    print(*line)