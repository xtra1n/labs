# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №6 ”Списки. Часть 1”
# 5. Поменять местами элементы с характеристиками по варианту. В-8
# 8. Первый нулевой и минимальный отрицательный.

index_zero = None
index_min_el = None
while index_zero is None or index_min_el is None:  # Выполняем программу пока пользователь не введет корректные данные
    index_zero = None
    index_min_el = None
    print('\nМассив должен содержать отрицательные и нулевые элементы !!!\n')
    arr = list(map(int, (input('Введите элементы списка: ').split())))  # Вводим массив

    for i in range(len(arr)):
        if arr[i] == 0 and index_zero is None:  # Проверяем первое вхождение нуля
            index_zero = i
        if arr[i] < 0 and (index_min_el is None or arr[index_min_el] > arr[i]):  # Провеярем первое вхождение минимального отрицательного
            index_min_el = i

arr[index_zero], arr[index_min_el] = arr[index_min_el], arr[index_zero]  # Меняем местами

print('\nИзмененный список: ', *arr)