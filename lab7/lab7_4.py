# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №7 “Списки. Часть 2”
# 4. Изменение элемента в списке строк по варианту.
# 8. Замена всех заглавных гласных английских букв на строчные

arr = list(map(str, input('Введите элементы списка: ').split()))

vowels_upper = 'AEIOUY'

for i in range(len(arr)):
    arr[i] = ''.join(char.lower() if char in vowels_upper else char for char in arr[i])
    # for symbol in vowels_upper:
    #     arr[i] = arr[i].replace(symbol, symbol.lower())

print('Измененный список: ', *arr)
