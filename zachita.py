# 

import math as m

x1,y1 = map(float, input('Введите значение x,y первой точки: ').split())
x2,y2 = map(float, input('Введите значение x,y второй точки: ').split())
x3,y3 = map(float, input('Введите значение x,y третьей точки: ').split())


epsilon = 1e-10
a = m.sqrt((x2 - x1)**2 + (y2 - y1)**2)
b = m.sqrt((x3 - x1)**2 + (y3 - y1)**2)
c = m.sqrt((x3 - x2)**2 + (y3 - y2)**2)


if not(a+b-c>epsilon and a+c-b>epsilon and b+c-a>epsilon):
    print('Точки не являются вершинами треугольника')
    exit()
    
    
degreeAB = m.acos((a**2+b**2-c**2)/(2*a*b))
degreeCB = m.acos((c**2+b**2-a**2)/(2*c*b))
degreeAC = m.acos((c**2+a**2-b**2)/(2*a*c))
p = (a + b + c)/2
s = m.sqrt(p*(p-a)*(p-b)*(p-c))
if degreeAB >= degreeCB and degreeAB >= degreeAC:
    h = 2 * s / c
if degreeCB >= degreeAB and degreeCB >= degreeAC:
    h = 2 * s / a
if degreeAC >= degreeCB and degreeAC >= degreeAB:
    h = 2 * s / b


print(f'\nДлины сторон a,b,c: {a:.5g}, {b:.5g}, {c:.5g}')
print(f'\nВысота из наибольшего угла: {h:.5g}')


    