# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №6 ”Списки. Часть 1”
# 1a. Добавить элемент в заданное место списка (по индексу) с использованием любых средств Python.

arr = list((input('Введите элементы массива: ').split()))
el = (input('Введите элемент, который нужно добавить: '))
index = int(input('Введите место, куда нужно добавить элемент: '))

while index <= 0:
    index = int(input('Введите положительный индекс, куда нужно добавить элемент: '))

arr.insert(index-1, el)
print('Измененный массив: ', *arr)