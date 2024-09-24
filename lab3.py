# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №3 ”Ьреугольник” 
# Длина сторон, биссектрисы из наибольшего угла по координатам трех точек


import math as m #Импортируем библиотеку math для вычеслений


x1 = float(input('Введите значение x первой точки: '))
y1 = float(input('Введите значение y первой точки: '))
x2 = float(input('Введите значение x второй точки: '))
y2 = float(input('Введите значение y второй точки: '))
x3 = float(input('Введите значение x третьей точки: '))
y3 = float(input('Введите значение y третьей точки: ')) #Запрашиваем координаты x,y трех точек на ввод


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


print(f'\nДлины сторон a,b,c: {a:.5g}, {b:.5g}, {c:.5g}') #Проверяем прямоугольный треугольник
if m.cos(degree1) == 0 or m.cos(degree2) == 0 or m.cos(degree3) == 0:
    print('Треугольник прямоугольный')
else:
    print('Треугольник не прямоугольный')


x=float(input('\nВведите координаты точки x: ')) #Запрашиваем координаты точки
y=float(input('Введите координаты точки y: '))  


s_original = abs(((x2-x1) * (y3-y1) - (x3-x1) * (y2-y1)) / 2) #Считаем площадь основного треугольника 
s1 = abs(((x2-x1)*(y-y1) + (x-x1) * (y2-y1)) / 2)
s2 = abs(((x-x1)*(y3-y1) + (x3-x1) * (y-y1)) / 2)
s3 = abs(((x2-x) * (y3-y) + (x3-x) * (y2-y)) / 2) #Считаем площади треугольников, образованных точкой
if s_original == s1 + s2 + s3:
    print('\nТочка принадлежит треугольнику') #Если площади малых треугольников равна площадь основного, то точка внутри
    point_inside = True
else:
    print('\nТочка не принадлежит треугольнику')
    point_inside = False
if point_inside:
    distance_to_side1 = (abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1) /  
                        m.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)) #Считаем растояние от точки до прямых по фоурмуле
    distance_to_side2 = (abs((y3 - y2) * x - (x3 - x2) * y + x3 * y2 - y3 * x2) /
                        m.sqrt((y3 - y2) ** 2 + (x3 - x2) ** 2))
    distance_to_side3 = (abs((y3 - y1) * x - (x3 - x1) * y + x3 * y1 - y3 * x1) / 
                        m.sqrt((y3 - y1) ** 2 + (x3 - x1) ** 2))
    distance_inside = min(distance_to_side1, distance_to_side2, distance_to_side3)
    print(f'Растояние до ближайшей стороны: {distance_inside:.5g}') #Выводим минимальное растояние до точки