# Леонтьев Андрей ИУ7-14Б
# 6. Дана матрица символов. Преобразовать её следующим образом: заменить все
# согласные латинские букв на заглавные, а все гласные латинские буквы на
# строчные. Вывести матрицу до преобразования и после.

# Вводим матрицу
width, length = list(map(int, input("Введите количество столбцоы и строк через пробел: ").split()))

while width < 1 or length < 1:
    print('Не верный размер матрицы')
    width, length = list(map(int, input("Введите количество столбцоы и строк через пробел: ").split()))

vowels = ['A', 'E', 'I', 'O', 'Y', 'U']

matrix = [[0]*width for _ in range(length)]

for i in range(length):
    for j in range(width):
        el = input(f'Введите {i+j+1}й элемент: ')
        if len(el) != 1:
            el = input('Введите символ: ')
        matrix[i][j] = el

print('Изначальная матрица:')    
for line in matrix:
    print(*line)

# Считаем
for i in range(length):
    for j in range(width):
        if matrix[i][j].isalpha():
            if matrix[i][j] in vowels:
                matrix[i][j] = matrix[i][j].lower()
            elif matrix[i][j].upper() in vowels:
                matrix[i][j] = matrix[i][j]
            else:
                matrix[i][j] = matrix[i][j].upper()

print('Измененная матрица')
for line in matrix:
    print(*line)