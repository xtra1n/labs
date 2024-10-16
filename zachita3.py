initial_value = float(input('Введите начальное значение аргумента: '))
final_value = float(input('Введите конечное значение аргумента: '))
step = float(input('Введите шаг печати: '))

while initial_value >= final_value:  # Проверяем введенные данные
    print('\nНачальное значение должно быть меньше конечного\n')
    initial_value = float(input('Введите начальное значение аргумента: '))
    final_value = float(input('Введите конечное значение аргумента: '))
while step > (final_value - initial_value):
    step = float(input('Введите шаг печати меньше разности конечного и начального значения: '))
while step <= 0:
    step = float(input('Введите положительный шаг печати: '))
    
max = None
min = None
cnt = int(abs((final_value - initial_value) / step)) + 1
x = initial_value

for i in range(cnt):
    y = 4 - x**2
    x += step
    if max is None or y > max:
        max = y
    if min is None or y < min:
        min = y
        
width = 88
scale = ((max - min) / width) if max > min else 0.5
distance = int(width / 2)

print(' ' * 8, f'{min:<.5g}{max:>{width}.5g}')

x = initial_value
pos_zero = int((0 - min) / scale) if min < 0 <= max else -1
for i in range(cnt):
    y = 4 - x**2
    print(f'{x:<8.2g}|', end = '')
    pos = int((y - min) / scale)
    for j in range(width + 1):
        if j == pos_zero:
            print('|', end = '')
        if j == pos:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
    x += step
 