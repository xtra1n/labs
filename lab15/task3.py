import struct
import os

def read_element(file, position, element_size):
    """Считывает элемент из бинарного файла."""
    file.seek(position * element_size)
    data = file.read(element_size)
    return struct.unpack('i', data)[0]  # Здесь предполагается, что данные типа int

def write_element(file, position, value, element_size):
    """Записывает элемент в бинарный файл."""
    file.seek(position * element_size)
    file.write(struct.pack('i', value))


def binary_search(file, element, start, end, element_size):
    """Находит правильную позицию для вставки с использованием бинарного поиска."""
    while start < end:
        mid = (start + end) // 2
        mid_value = read_element(file, mid, element_size)
        if element < mid_value:
            end = mid
        else:
            start = mid + 1
    return start

def binary_insertion_sort(filename):
    """Сортирует бинарный файл методом бинарной вставки."""
    element_size = struct.calcsize('i')  # Размер одного элемента в байтах

    with open(filename, 'r+b') as file:
        # Получаем количество элементов в файле
        file.seek(0, os.SEEK_END)
        file_size = file.tell()
        num_elements = file_size // element_size

        for i in range(1, num_elements):
            current_value = read_element(file, i, element_size)
            # Находим позицию для вставки текущего элемента
            insert_pos = binary_search(file, current_value, 0, i, element_size)

            # Сдвигаем элементы вправо для освобождения места
            for j in range(i, insert_pos, -1):
                prev_value = read_element(file, j - 1, element_size)
                write_element(file, j, prev_value, element_size)

            # Вставляем текущий элемент на правильную позицию
            write_element(file, insert_pos, current_value, element_size)