# Леонтьев Андрей
# ИУ7-14Б
# Лабораторная работа №6 ”Списки. Часть 1”
# 5. Поменять местами элементы с характеристиками по варианту. В-8
# 8. Первый нулевой и минимальный отрицательный.

print('Список должен содержать отрицательные и нулевые элементы')
arr = list(map(int, (input('Введите элементы списка: ').split())))  # Вводим элементы списка
index_zero = None
min_el = None


for i in range(len(arr)):  # Проходимся по списку и ищем первый ноль и первый минимальный
    if arr[i] == 0 and index_zero is None:
        index_zero = i
    if (arr[i] < 0 and arr[min_el] > arr[i]) or min_el is None:
        min_el = i
        
if index_zero is None or min_el is None:  # Выводим сообщение, если нет нужных элементов
    print('Не нашлось необходимых значений')
    exit()

arr[index_zero], arr[min_el] = arr[min_el], arr[index_zero]  # Меняем местами элементами

print('Измененный список: ', *arr)  # Выводим список