# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №2 ”Написание алгоритмов с выбором условий” Часть 2.
# В-2. Принадлежность точки область по x,y

#Импортируем библиотеку math
import math as m 

#Запрашиваем x,y на ввод
x = float(input('Введите значение x: '))
y = float(input('Введите значение y: '))


if y >= 0 and y <= -2*x+4 and y >= (-1/4)*x**2+1 and y <= 2*x+4:
    flag = True
    print(f'Точка x={x}, y={y} принадлежит области') 
elif y < 0 and y <= (-1/4)*x**2+1 and y >= min(2*x+4,-2*x+4):
    print(f'Точка x={x}, y={y} принадлежит области') 
else:
    print(f'Точка x={x}, y={y} не принадлежит области')