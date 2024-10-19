# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №6 ”Списки. Часть 1”
# Найти значение K-го экстремума в списке.

arr = list(map(int, (input('Введите элементы списка: ').split())))  # Запрашиваем данные на ввод
index_extr = int(input('Введите номер экстремума: '))
cnt = 0
flag = False

while index_extr > len(arr) or index_extr <= 0:  # Провеярем коректность данных
        print('Номер экстремума не может быть больше или меньше длины списка')
        index_extr = int(input('Введите номер экстремума: '))
    
for i in range(index_extr,len(arr) - 1):
    if ((arr[i-1] < arr[i]  and arr[i] > arr[i+1]) or
        (arr[i-1] > arr[i] and arr[i] < arr[i+1])):  # Проверяем является элемент экстремумом
        cnt += 1  # Считаем его номер
        if cnt == index_extr:  # Если номер совпал с необходимым - выводим
            print(f'Экстремум №{index_extr}:', arr[i])
            flag = True
            break
if not flag:
    print('Экстремума с таким номером не нашлось')