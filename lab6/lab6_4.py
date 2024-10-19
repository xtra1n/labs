# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №6 ”Списки. Часть 1”
# 4. Найти наиболее длинную непрерывную последовательность по варианту. В-4
# 4. Убывающая последовательность простых чисел.

arr = list(map(int, (input('Введите элементы списка: ').split())))  # Запрашиваем данные на ввод
subsequence = []
previous_is_prime = all(arr[0] % n != 0 for n in range(2, int(arr[0] ** 0.5) + 1))  # Проверяем первый элемент на простоту
prime_numbers = [arr[0]] if previous_is_prime else []

for i in range(1,len(arr)):
    if (all(arr[i] % n != 0 for n in range(2, int(arr[i] ** 0.5) + 1)) and
        arr[i] > 1):  # Проверяем на простоту числа
        if previous_is_prime and arr[i] < arr[i-1]:  # Проверяем наличие убывающей последовательности
            prime_numbers.append(arr[i-1]) if len(prime_numbers) == 0 else prime_numbers  # Если первый элемент последовательности добавляем его
            prime_numbers.append(arr[i])
        previous_is_prime = True  # Запоминаем простоту числа
    else:
        previous_is_prime = False
        subsequence.append(prime_numbers)  # Добавляем последовательность в список
        prime_numbers = []
            
print('Максимальная длина последовательности: ', max(subsequence, key = len))