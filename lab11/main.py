"""
Леонтьев Андрей ИУ7-14Б

Написать программу для демонстрации работы метода сортировки (по варианту) на
примере массива целых чисел.
Программа должна состоять из двух частей (этапов работы) и выполнять
два действия
последовательно:
1. сначала отсортировать заданный пользователем массив для доказательства
корректности работы алгоритма;
2. затем составить таблицу замеров времени сортировки списков трёх различных
(заданных пользователем) размерностей и количества перестановок в каждом
из них.
В части 2 для каждой размерности списка необходимо исследовать:
● случайный список,
● отсортированный список,
● список, отсортированный в обратном порядке
Вставка бинарным поиском
"""


from utils import get_arr, get_int, generate_arr, output
from sort_util import binary_insertionsort


def main():
    """
    Основная функция
    """
    n = get_int('Введите размерность массива: ', False)
    arr = get_arr(n)
    arr, t, cnt = binary_insertionsort(arr)

    print('Сортированный массив: ', *arr)

    n_1 = get_int('Введите размерность 1: ', False)
    n_2 = get_int('Введите размерность 2: ', False)
    n_3 = get_int('Введите размерность 3: ', False)

    arr_1 = generate_arr(n_1)
    arr_2 = generate_arr(n_2)
    arr_3 = generate_arr(n_3)

    sorted_arr_1 = sorted(arr_1)
    sorted_arr_2 = sorted(arr_2)
    sorted_arr_3 = sorted(arr_3)

    reversed_arr_1 = sorted(arr_1, reverse=True)
    reversed_arr_2 = sorted(arr_2, reverse=True)
    reversed_arr_3 = sorted(arr_3, reverse=True)

    arr1, t1, cnt1 = binary_insertionsort(sorted_arr_1)
    arr2, t2, cnt2 = binary_insertionsort(sorted_arr_2)
    arr3, t3, cnt3 = binary_insertionsort(sorted_arr_3)

    arr4, t4, cnt4 = binary_insertionsort(arr_1)
    arr5, t5, cnt5 = binary_insertionsort(arr_2)
    arr6, t6, cnt6 = binary_insertionsort(arr_3)

    arr7, t7, cnt7 = binary_insertionsort(reversed_arr_1)
    arr8, t8, cnt8 = binary_insertionsort(reversed_arr_2)
    arr9, t9, cnt9 = binary_insertionsort(reversed_arr_3)

    output(t1, cnt1, t2, cnt2, t3, cnt3, t4, cnt4, t5, cnt5, t6, cnt6, t7,
           cnt7, t8, cnt8, t9, cnt9)


if __name__ == '__main__':
    main()
