import struct

def sort_binary_file(filename):
    size_of_long_long = struct.calcsize('q')  # Размер одного числа long long (8 байт)

    with open(filename, 'r+b') as file:
        # Определяем количество чисел в файле
        file.seek(0, 2)  # Переходим в конец файла
        file_size = file.tell()  # Размер файла в байтах
        num_count = file_size // size_of_long_long  # Количество чисел

        # Реализация сортировки методом выбора
        for i in range(num_count):
            min_index = i
            # Найти индекс минимального элемента в оставшейся части
            for j in range(i + 1, num_count):
                # Чтение числа на позиции min_index
                file.seek(min_index * size_of_long_long)
                min_value = struct.unpack('q', file.read(size_of_long_long))[0]

                # Чтение числа на позиции j
                file.seek(j * size_of_long_long)
                current_value = struct.unpack('q', file.read(size_of_long_long))[0]

                if current_value < min_value:
                    min_index = j

            # Обмен значений i и min_index, если min_index изменился
            if min_index != i:
                # Чтение значения на позиции i
                file.seek(i * size_of_long_long)
                value_i = struct.unpack('q', file.read(size_of_long_long))[0]

                # Чтение значения на позиции min_index
                file.seek(min_index * size_of_long_long)
                value_min = struct.unpack('q', file.read(size_of_long_long))[0]

                # Запись значения value_min на позицию i
                file.seek(i * size_of_long_long)
                file.write(struct.pack('q', value_min))

                # Запись значения value_i на позицию min_index
                file.seek(min_index * size_of_long_long)
                file.write(struct.pack('q', value_i))

def print_binary_file(filename):
    size_of_long_long = struct.calcsize('q')
    with open(filename, 'rb') as file:
        while chunk := file.read(size_of_long_long):
            number = struct.unpack('q', chunk)[0]
            print(number, end=' ')
    print()

# Пример использования
filename = 'numbers.bin'

# Создание тестового файла
with open(filename, 'wb') as file:
    numbers = [5, 1, 4, 2, 3]
    for number in numbers:
        file.write(struct.pack('q', number))

# Сортировка файла
sort_binary_file(filename)

# Вывод содержимого файла
print("Содержимое файла после сортировки:")
print_binary_file(filename)
