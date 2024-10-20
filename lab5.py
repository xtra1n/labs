# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №4 ”График”
# В-50
# z1 = a**3 - 19.1*a**2 + 27.9*a + 5.58
# z2 = a**2 - sin(pi*a)
# Доп. задание: Найти сумму положительный значений  z2
# График по z2

import math as m

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
    
a = initial_value  # Задаем значение аргумента
max = None  # Вводим максимальный элемент последовательности
min = None  # Вводим минимальный элемент последовательности
cnt = int(abs((final_value - initial_value) / step)) + 1  # Вводим счетчик для подсчета количества операций
sum_z2 = 0  # Сумма положительных значений функции z2

print('\n----------------------------------------')  # Рисуем талицу значений
print(f'|{"a":^{12}}|{"z1":^{12}}|{"z2":^{12}}|')
print('----------------------------------------')
for i in range(cnt):
    z1 = a**3 - 19.1*a**2 + 27.9*a + 5.58
    z2 = a**2 - m.sin(m.pi*a)
    print(f'|{i}{a:^12.5g}|{z1:^12.5g}|{z2:^12.5g}|')
    a += step
    if z2 > max or max is None:  # Ищем максимальный элемент
        max = z2
    if z2 < min or min is None:  # Ищем минимальный элемент
        min = z2
    if z2 > 0:
        sum_z2 += z2
print('----------------------------------------')

print(f'Сумма положительных значений: {sum_z2:.5g}')

notch = int(input('Введите количество засечек (4-8): '))  # Запрашиваем количество засечек
width = 88
scale = (max - min) / width  # Считаем масштаб

while notch < 4 or notch > 8:  # Проверяем корректность данных
    notch = int(input('\nВведите количество засечек (4-8): \n'))
if abs(max - min) < 1e-20:
    print('Ввденные данные некоректны.')
    exit()

print(' ' * 8, end = '')  # Делаем отступ для верхней шкалы
print(f'{min:.5g}', end = '')  # Выводим минимальный элемент
distance = int(width / (notch-1))  # Считаем растояние между засечками
for i in range(1, notch):
    tick = min + i*(max - min)/(notch - 1)  # Считаем значение засечек
    print(f'{tick:{distance}.5g}', end = ' ')  # Выводим все остальные засечки
print()

a = initial_value  # Заново вводим переменную
for i in range(cnt):  # Строим график второй z2
    z2 = a**2 - m.sin(m.pi*a)
    print(f'{a:<8.2g}|', end = '')  # Выводим значение переменной
    pos = (int((z2 - min)/scale))  # Считаем позицию точки
    pos_zero = int((0 - min)/(scale)) if min <= 0 <= max else -1  # Считаем позицию оси абцисс
    for j in range(width+1):  # Проходим по всей длине графика
        if j == pos_zero:
            print('|', end = '')  # Рисуем ось абцисс
        elif j == pos:
            print('*', end = '')  # Ставим точку на нужных позициях
        else:
            print(' ', end = '')
    print()
    a += step
