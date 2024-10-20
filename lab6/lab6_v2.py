# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №6 ”Списки. Часть 1”
# 5. Поменять местами элементы с характеристиками по варианту. В-8
# 8. Первый нулевой и минимальный отрицательный.

index_zero = -1#None
index_min_el = -1 

while index_zero == -1 or index_min_el == -1:  # Выполняем программу пока пользователь не введет корректные данные
    index_zero = -1
    index_min_el = -1

    print('\nМассив должен содержать отрицательные и нулевые элементы !!!\n')
    arr = list(map(int, (input('Введите элементы списка: ').split())))  # Вводим массив

    for i in range(len(arr)):
        if arr[i] == 0 and index_zero == -1:  # Проверяем первое вхождение нуля
            index_zero = i
            break
    for i in range(len(arr)):    
        if arr[i] < 0 and (index_min_el == -1 or arr[index_min_el] > arr[i]):  # Провеярем первое вхождение минимального отрицательного
            index_min_el = i
            break

arr[index_zero], arr[index_min_el] = arr[index_min_el], arr[index_zero]  # Меняем местами

print('\nИзмененный список: ', *arr)