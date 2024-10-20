# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №6 ”Списки. Часть 1”
# 4. Найти наиболее длинную непрерывную последовательность по варианту. В-4
# 4. Убывающая последовательность простых чисел.


arr = list(map(int, input('Введите элементы списка: ').split()))  # Запрашиваем данные на ввод

start_index = -1  # Начальный индекс последовательности
max_length = 0  # Максимальная длина последовательности
max_start_index = 0  # Индекс начала максимальной последовательности

previous_is_prime = all(arr[0] % n != 0 for n in range(2, int(arr[0] ** 0.5) + 1))  # Проверяем первый элемент на простоту

for i in range(len(arr)):
    if (all(arr[i] % n != 0 for n in range(2, int(arr[i] ** 0.5) + 1)) and
        arr[i] > 1):  # Проверяем на простоту числа
        if previous_is_prime and (start_index == -1 or arr[i] < arr[i-1]):  # Убывающая последовательность
            if start_index == -1:
                start_index = i - 1  # Запоминаем начальный индекс последовательности

        if start_index != -1:
            if arr[i] >= arr[i-1]:  # Если последовательность прерывается
                length = i - start_index  # Подсчет длины текущей последовательности
                if length > max_length:
                    max_length = length
                    max_start_index = start_index  # Обновляем индекс начала максимальной последовательности
                start_index = -1  # Сбрасываем начальный индекс
    else:
        if previous_is_prime and start_index != -1:  # Конец последовательности
            length = i - start_index  
            if length > max_length:
                max_length = length
                max_start_index = start_index
            start_index = -1  # Сбрасываем начальный индекс

    previous_is_prime = all(arr[i] % n != 0 for n in range(2, int(arr[i] ** 0.5) + 1))  # Обновляем флаг простоты

# Проверим в конце, если последовательность закончилась именно на простом числе
if start_index != -1:
    length = len(arr) - start_index
    if length > max_length:
        max_length = length
        max_start_index = start_index

# Вывод максимальной последовательности
if max_length > 0:
    print('Максимальная последовательность простых чисел:', *arr[max_start_index:max_start_index + max_length])
else:
    print('Простых чисел в последовательности не найдено')
