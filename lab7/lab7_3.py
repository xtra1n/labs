# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №7 “Списки. Часть 2”
# 3. Поиск элемента в списке строк по варианту.
# Поиск элемента наибольшей длины, не содержащего цифр

arr = list(map(str, input('Введите элементы списка: ').split()))

result = 'Отсутствует'
max_len = -1

for el in arr:
    if ((not(any((char.isdigit()) for char in el))) and
        (len(el) > max_len)):
        result = el
        max_len = len(el)

print('Строка наибольшей длины без цифр: ', result)