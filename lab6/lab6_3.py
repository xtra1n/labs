# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №6 ”Списки. Часть 1”
# Найти значение K-го экстремума в списке.

arr = list((input('Введите элементы массива: ').split()))
index = int(input('Введите номер экстремума: '))
cnt = 0

while index <= 0:
    index = int(input('Введите положительный индекс, куда нужно добавить элемент: '))
    
for i in range(index,len(arr) - 1):
    if (arr[i] == max(arr[i], arr[i-1], arr[i + 1])
        or arr[i] == min(arr[i], arr[i-1], arr[i + 1])):
        cnt += 1
        if cnt == index:
            print(f'Экстремум №{index}:', arr[i])
            break
