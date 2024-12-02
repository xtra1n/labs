import time


def binary_insertionsort(arr):
    """
    Функция для вставки
    """
    start = time.time()
    cnt = 0
    for i in range(1, len(arr)):
        temp = arr[i]
        pos = binary_search(arr, temp, 0, i) + 1

        for k in range(i, pos, -1):
            arr[k] = arr[k - 1]

        if arr[pos] != temp:
            cnt += 1
        arr[pos] = temp

    finish = time.time()
    work_time = finish - start
    return arr, work_time * 1000, cnt


def binary_search(arr, key, strt, end):
    """
    Функция для бинарного поиска места
    """
    while end - strt > 1:
        middle = (strt + end) // 2
        if arr[middle] < key:
            strt = middle
        elif arr[middle] > key:
            end = middle
        else:
            return middle

    if key < arr[strt]:
        return strt - 1
    else:
        return strt
