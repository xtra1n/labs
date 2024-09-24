# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №3 ”Ьреугольник” 
# Длина сторон, биссектрисы из наибольшего угла по координатам трех точек


import math as m #Импортируем библиотеку math для вычеслений

#Запрашиваем координаты x,y трех точек на ввод
x1 = float(input('Введите значение x первой точки: '))
y1 = float(input('Введите значение y первой точки: '))
x2 = float(input('Введите значение x второй точки: '))
y2 = float(input('Введите значение y второй точки: '))
x3 = float(input('Введите значение x третьей точки: '))
y3 = float(input('Введите значение y третьей точки: '))


a = m.sqrt((x2-x1)**2+(y2-y1)**2) 
b = m.sqrt((x3-x1)**2+(y3-y1)**2)
c = m.sqrt((x3-x2)**2+(y3-y2)**2) #Вычисляем длины сторон a,b,c
degree1 = m.acos((a**2+b**2-c**2)/(2*a*b)) #Вычисляем угол между a и b 
degree2 = m.acos((c**2+b**2-a**2)/(2*c*b)) #Вычисляем угол между b и c
degree3 = m.acos((c**2+a**2-b**2)/(2*a*c)) #Вычисляем угол между a и c 
if degree1 == max(degree1,degree2,degree3):
    l = (2*b*a*m.cos(degree1/2))/(b+a)
elif degree2 == max(degree1,degree2,degree3):
    l = (2*b*c*m.cos(degree2/2))/(b+c)
else:
    l = (2*a*c*m.cos(degree3/2))/(a+c) #Вычисляем биссектрису при наибольшем угле


print(f'\nДлины сторон a,b,c: {a:.5g}, {b:.5g}, {c:.5g}')
if m.cos(degree1) == 0 or m.cos(degree2) == 0 or m.cos(degree3) == 0:
    print('Треугольник прямоугольный')
else:
    print('Треугольник не прямоугольный')



x=float(input('\nВведите координаты точки x: '))
y=float(input('Введите координаты точки y: '))  


if ((x1-x)*(y2-y1)-(x2-x1)*(y1-y) >= 0) and
(x2-x)*(y3-y2)-(x3-x2)*(y2-y) >= 0 and (x3-x0)*(y1-y3)-(x1-x3)*(y3-y0) >= 0:
    pass