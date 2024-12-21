import struct

def read_number(file, index):
    """Считывает число из файла по указанному индексу."""
    file.seek(index * 8)
    return struct.unpack('q', file.read(8))[0]

def write_number(file, index, number):
    """Записывает число в файл по указанному индексу."""
    file.seek(index * 8)
    file.write(struct.pack('q', number))

def get_file_length(file):
    """Возвращает количество чисел в файле."""
    file.seek(0, 2)  # Переместить указатель в конец файла
    return file.tell() // 8

def insertion_sort_binary_file(filename):
    """Сортирует бинарный файл методом простых вставок."""
    with open(filename, 'r+b') as file:
        length = get_file_length(file)
        
        for i in range(1, length):
            # Считать текущее число
            current = read_number(file, i)
            
            # Найти место для вставки
            j = i - 1
            while j >= 0 and read_number(file, j) > current:
                # Сдвиг числа на одну позицию вправо
                temp = read_number(file, j)
                write_number(file, j + 1, temp)
                j -= 1

            # Вставить текущее число на нужную позицию
            write_number(file, j + 1, current)

def print_binary_file(filename):
    """Выводит содержимое бинарного файла в виде чисел."""
    with open(filename, 'rb') as file:
        length = get_file_length(file)
        numbers = [read_number(file, i) for i in range(length)]
        print(numbers)

# Пример использования
filename = 'numbers.bin'

# Создание тестового файла
with open(filename, 'wb') as f:
    numbers = [42, -5, 17, 0, 99, -100]
    for number in numbers:
        f.write(struct.pack('q', number))

print("Файл до сортировки:")
print_binary_file(filename)

insertion_sort_binary_file(filename)

print("Файл после сортировки:")
print_binary_file(filename)
