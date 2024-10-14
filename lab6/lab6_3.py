# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №6 ”Списки. Часть 1”
# Найти значение K-го экстремума в списке.

arr = list(map(int, (input('Введите элементы массива: ').split())))
index = int(input('Введите номер экстремума: '))
cnt = 0
flag = False

while index > len(arr):
    print('Номер экстремума не может быть больше длины массива')
    index = int(input('Введите номер экстремума: '))
while index <= 0:
    index = int(input('Введите положительный индекс, куда нужно добавить элемент: '))
    
for i in range(index,len(arr) - 2):
    if (arr[i-1] < arr[i] > arr[i+1] or
        arr[i-1] > arr[i] < arr[i+1]):
        cnt += 1
        if cnt == index:
            print(f'Экстремум №{index}:', arr[i])
            flag = True
            break
if not flag:
    print('Экстремума с таким номером не нашлось')