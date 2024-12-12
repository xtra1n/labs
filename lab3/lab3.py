# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №3 ”Ьреугольник” 
# Длина сторон, биссектрисы из наибольшего угла по координатам трех точек


import math as m #Импортируем библиотеку math для вычеслений

x1,y1 = map(float, input('Введите значение x,y первой точки: ').split())
x2,y2 = map(float, input('Введите значение x,y второй точки: ').split())
x3,y3 = map(float, input('Введите значение x,y третьей точки: ').split()) #Запрашиваем координаты x,y трех точек на ввод


epsilon = 1e-10 #Вводим погрешность
a = m.sqrt((x2-x1)**2+(y2-y1)**2) 
b = m.sqrt((x3-x1)**2+(y3-y1)**2)
c = m.sqrt((x3-x2)**2+(y3-y2)**2) #Вычисляем длины сторон a,b,c
if not(a+b-c>epsilon and a+c-b>epsilon and b+c-a>epsilon):
    print('Точки не являются вершинами треугольника')
    exit()


degree1 = m.acos((a**2+b**2-c**2)/(2*a*b)) #Вычисляем угол между a и b 
degree2 = m.acos((c**2+b**2-a**2)/(2*c*b)) #Вычисляем угол между b и c
degree3 = m.acos((c**2+a**2-b**2)/(2*a*c)) #Вычисляем угол между a и c 
if degree1 >= degree2 and degree1 >= degree2: #Вычисляем биссектрису при наибольшем угле
    l = (2*b*a*m.cos(degree1/2))/(b+a)
elif degree2 >= degree1 and degree2 >= degree3:
    l = (2*b*c*m.cos(degree2/2))/(b+c)
else:
    l = (2*a*c*m.cos(degree3/2))/(a+c) 


print(f'\nДлины сторон a,b,c: {a:.5g}, {b:.5g}, {c:.5g}') #Проверяем прямоугольный треугольник
if abs(m.cos(degree1)) <= epsilon or abs(m.cos(degree2)) <= epsilon or abs(m.cos(degree3)) <= epsilon:
    print('Треугольник прямоугольный')
else:
    print('Треугольник не прямоугольный')


x,y = map(float, input('Введите координаты точки: ').split()) #Запрашиваем координаты точки
 


s_original = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2) #Считаем площадь основного треугольника (Формула Герона)
s1 = abs((x*(y1-y2) + x1*(y2-y) + x2*(y-y1)) / 2)
s2 = abs((x*(y2-y3) + x2*(y3-y) + x3*(y-y2)) / 2)
s3 = abs((x*(y3-y1) + x3*(y1-y) + x1*(y-y3)) / 2) #Считаем площади треугольников, образованных точкой
if s_original - (s1 + s2 + s3) <= epsilon:
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
    if distance_to_side1 <= distance_to_side2 and distance_to_side1<=distance_to_side3:
        distance_inside = distance_to_side1
    if distance_to_side2 <= distance_to_side1 and distance_to_side2<=distance_to_side3:
        distance_inside = distance_to_side2
    if distance_to_side3 <= distance_to_side2 and distance_to_side3<=distance_to_side1:
        distance_inside = distance_to_side3
    print(f'Растояние до ближайшей стороны: {distance_inside:.5g}') #Выводим минимальное растояние до точки
    
    