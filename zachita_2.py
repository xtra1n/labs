x = float(input('Введите значение аргумента: '))
eps = float(input('Введите значение точности: '))
iterations = int(input('Введите количество итераций: '))

while iterations <= 0:
    iterations = int(input('Введите положительное количество итераций: '))
while eps <= 0:
    eps = float(input('Введите положительную погрешность: '))

cnt = 0
n = 1
arg = 1
summa = arg

while cnt <= iterations and  abs(arg*n) > eps:
    cnt += 1
    arg *= x**2 / (n) / (n+1)
    summa += (-1)**(cnt+1)*arg*n
    n += 2
else:
    if cnt > iterations:  
        print('\nЗа указанное число итераций необходимой точности достичь не удалось')  
    else:
        print('----------------------------------------')
        print(f'\nСумма равна: {summa:.5g}')
