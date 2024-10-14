# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №6 ”Списки. Часть 1”
# 5. Поменять местами элементы с характеристиками по варианту. В-8
# 8. Первый нулевой и минимальный отрицательный.

index_zero = None
min_el = None
while index_zero is None or min_el is None:
    index_zero = None
    min_el = None
    print('\nМассив должен содержать отрицательные и нулевые элементы !!!\n')
    arr = list(map(int, (input('Введите элементы массива: ').split())))

    for i in range(len(arr)):
        if arr[i] == 0 and index_zero is None:
            index_zero = i
        if arr[i] < 0 and (min_el is None or arr[min_el] > arr[i]):
            min_el = i
else:
    arr[index_zero], arr[min_el] = arr[min_el], arr[index_zero]

    print('\nИзмененный массив: ', *arr)