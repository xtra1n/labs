# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №4 ”Сумма ряда”
# В-109
# sum = -x/1 + -x**2/2 - ... - x**n/n

import math as m

initial_value = float(input('Введите начальное значение аргумента: '))
final_value = float(input('Введите конечное значение аргумента: '))
step = float(input('Введите шаг печати: '))

if initial_value > final_value or step <= 0:
    print('Введенные данные некорректны')
    exit()

a = initial_value
max = -1e10
min = 1e10
cnt=0
print('\n----------------------------------------') # Рисуем талицу значений
print(f'|{"a":^{12}}|{"z1":^{12}}|{"z2":^{12}}|')
print('----------------------------------------')
while a <= final_value:
    z1 = a**2
    z2 = a**2 - m.sin(m.pi*a)
    print(f'|{a:^12.5g}|{z1:^12.5g}|{z2:^12.5g}|')
    a += step
    if z2 > max:
        max = z2
    if z2 < min:
        min = z2
    cnt+=1
print('----------------------------------------')

notch = int(input('Введите количество засечек (4-8): '))

if notch < 4 or notch > 8:
    print('Введено неверное количество засечек')
    exit()
    
print(' '*6,end='')
print(f'{min:.5g}',end='')
t = int(80 / (notch-1))
for i in range(1,notch):
    tick = min + i*(max-min)/(notch - 1)
    print(f'{tick:{t}.5g}',end=' ')
print()

h = (max-min)/79
a = initial_value
for i in range(cnt):
    z2 = a**2 - m.sin(m.pi*a)
    print(f'{a:<5g}|',end='')
    pos = (int((z2 - min)/h))
    
    pos_zero = int((0-min)/(h)) if min <= 0 <= max else -1

 
    
    for j in range(80):
        if j == pos:
            print('*',end='')
        elif j == pos_zero:
            print('|',end='')
        else:
            print(' ',end='')
    print()
    a += step


