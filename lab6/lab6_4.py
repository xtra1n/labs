# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №6 ”Списки. Часть 1”
# 4. Найти наиболее длинную непрерывную последовательность по варианту. В-4
# 4. Убывающая последовательность простых чисел.

arr = list(map(int, (input('Введите элементы списка: ').split())))  # Запрашиваем данные на ввод
cnt = 0
max_len = 0
previous_is_prime = all(arr[0] % n != 0 for n in range(2, arr[0]//2))  # Проверяем первый элемент на простоту

for i in range(1,len(arr)):
    if (all(arr[i] % n != 0 for n in range(2, arr[i]//2 + 1)) and
        arr[i] > 1):  # Проверяем на простоту числа
        if previous_is_prime and arr[i] < arr[i-1]:  # Проверяем наличие убывающей последовательности
            cnt += 1
        else:
            max_len = max(cnt, max_len)  # Присваем максимальный элемент, если последовательность прервалась
            cnt = 0
            previous_is_prime = False
        previous_is_prime = True  # Запоминаем простоту числа
    max_len = max(cnt, max_len)
print('Максимальная длина последовательности: ', max_len + 1 if max_len > 0
      else 'Последовательности не нашлось')