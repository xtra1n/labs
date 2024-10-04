# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №4 ”График”
# В-50
# z1 = a**3 - 19.1*a**2 + 27.9*a + 5.58
# z2 = a**2 - sin(pi*a)

import math as m

initial_value = float(input('Введите начальное значение аргумента: '))
final_value = float(input('Введите конечное значение аргумента: '))
step = float(input('Введите шаг печати: '))

if initial_value > final_value or step <= 0:  # Проверяем введенные данные
    print('Введенные данные некорректны')
    exit()

a = initial_value  # Задаем значение аргумента
max = -1e10  # Вводим максимальный элемент последовательности
min = 1e10  # Вводим минимальный элемент последовательности
cnt=0  # Вводим счетчик для подсчета количества операций

print('\n----------------------------------------')  # Рисуем талицу значений
print(f'|{"a":^{12}}|{"z1":^{12}}|{"z2":^{12}}|')
print('----------------------------------------')
while a <= final_value:
    z1 = a**3 - 19.1*a**2 + 27.9*a + 5.58
    z2 = a**2 - m.sin(m.pi*a)
    print(f'|{a:^12.5g}|{z1:^12.5g}|{z2:^12.5g}|') 
    a += step
    if z2 > max:  # Ищем максимальный элемент
        max = z2
    if z2 < min:  # Ищем минимальный элемент
        min = z2
    cnt += 1
print('----------------------------------------')

notch = int(input('Введите количество засечек (4-8): '))  # Запрашиваем количество засечек

if notch < 4 or notch > 8:  # Проверяем корректность данных
    print('\nВведено неверное количество засечек\n')
    exit()
    
print(' ' * 6, end = '')  # Делаем отступ для верхней шкалы
print(f'{min:.5g}', end = '')  # Выводим минимальный элемент 
distance = int(80 / (notch-1))  # Считаем растояние между засечками
for i in range(1, notch):
    tick = min + i*(max - min)/(notch - 1)  # Считаем значение засечек
    print(f'{tick:{distance}.5g}', end = ' ')  # Выводим все остальные засечки
print()

scale = (max - min) / 80  # Считаем масштаб
a = initial_value  # Заново вводим переменную

for i in range(cnt):  # Строим график второй z2
    z2 = a**2 - m.sin(m.pi*a)  
    print(f'{a:<5g}|', end = '')  # Выводим значение переменной
    pos = (int((z2 - min)/scale))  # Считаем позицию точки
    pos_zero = int((0 - min)/(scale)) if min <= 0 <= max else -1  # Считаем позицию оси абцисс
    for j in range(80):  # Проходим по всей длине графика
        if j == pos:
            print('*', end = '')  # Ставим точку на нужных позициях
        elif j == pos_zero:
            print('|', end = '')  # Рисуем ось абцисс
        else:
            print(' ', end = '')
    print()
    a += step

