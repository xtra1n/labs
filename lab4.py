# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №4 ”Сумма ряда”
# В-109


x = float(input('Введите значение аргумента: '))  # Запрашиваем необохдимые данные на ввод
e = float(input('Введите значение точности: '))
iterations = int(input('Введите количество интераций: '))
t = int(input('Введите шаг печати: '))


cnt = 1  # Вводим счетчик итераций
i = 2  # Вводим изменяющуюся переменную
eps = 1e-10  # Вводим погрешность
arg = -x  # Введем значение аргумента
s = arg  # Вводим значение суммы


print(f'{"Итерации":^{12}}{"Аргумент":^{12}}{"Сумма":^{12}}')  # Выводим первую строку таблицы


while (cnt <= iterations and  abs(arg) > e and
    ((x >= eps and abs(arg + e) > eps) or
    (x < eps and abs(arg - e) > eps))):
    if (cnt - 1) % t == 0:
        print(f'{cnt:^12.5g}{arg:^12.5g}{s:^12.5g}')  # Выводим значения с указанным шагом
    arg = (-1) * x ** i / i
    s += arg
    i += 1
    cnt += 1
else:  # Выводим конечную сумму
    if cnt == 1:
        print(f'{cnt:^12.5g}{arg:^12.5g}{s:^12.5g}')
    if cnt > iterations:  
        print('За указанное число итераций необходимой точности достичь не удалось')  
    else:
        print(f'Сумма равна: {s:.5g}')
   