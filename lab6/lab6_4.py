# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №6 ”Списки. Часть 1”
# 4. Найти наиболее длинную непрерывную последовательность по варианту. В-4
# 4. Убывающая последовательность простых чисел.

arr = list(map(int, (input('Введите элементы массива: ').split())))
cnt = 0
max_len = 0

for i in range(1,len(arr)):
    if (1 < arr[i] < arr[i-1] and
        all(arr[i] % n != 0 for n in range(2,arr[i]//2)) and
        all(arr[i-1] % n != 0 for n in range(2,arr[i-1]//2))):
        cnt += 1
    else:
        max_len = max(cnt, max_len)
        cnt = 0
print('Максимальная длина последовательности: ', max_len + 1)