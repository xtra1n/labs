# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №7 “Списки. Часть 2”
# 1. Удалить все элементы целочисленного списка, имеющие свойство по варианту, за один цикл. Без del pop remove срезов
# Положительные элементы

arr = list(map(int, input('Введите элементы списка: ').split()))

ind_plus = 1
ind_minus = 0

for i in range(len(arr)):
    if arr[i] <= 0:
        arr[ind_minus] = arr[i]
        ind_minus += 1
    else:
        ind_plus += 1

if ind_plus != 1:
    arr = arr[:ind_minus]

print('Измененный список: ', *arr)
