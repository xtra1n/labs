import struct

# Открытие файла для чтения и записи
with open('numbers.bin', 'r+b') as f:
    # Определяем размер одного числа (8 байт)
    num_size = struct.calcsize('q')
    
    # Получаем общий размер файла
    f.seek(0, 2)  # Переходим в конец файла
    file_size = f.tell()
    
    # Вычисляем количество чисел и позицию середины
    num_count = file_size // num_size
    half = num_count // 2
    
    # Позиции для первой и второй половины
    first_half_pos = 0
    second_half_pos = half * num_size

    # Переворачиваем первую половину и меняем местами с второй половиной
    for i in range(half):
        # Читаем элементы из первой половины
        f.seek(first_half_pos + i * num_size)
        first_half_value = struct.unpack('q', f.read(num_size))[0]

        # Читаем элементы из второй половины
        f.seek(second_half_pos + i * num_size)
        second_half_value = struct.unpack('q', f.read(num_size))[0]
        
        # Записываем элементы на их новые позиции
        f.seek(first_half_pos + i * num_size)
        f.write(struct.pack('q', second_half_value))
        
        f.seek(second_half_pos + i * num_size)
        f.write(struct.pack('q', first_half_value))

    # Если количество чисел нечетное, то среднее число остается на своем месте
    if num_count % 2 != 0:
        middle_pos = half * num_size
        f.seek(middle_pos)
        middle_value = struct.unpack('q', f.read(num_size))[0]
        f.seek(middle_pos)
        f.write(struct.pack('q', middle_value))
    
# Для проверки, откроем файл и выведем его содержимое
with open('numbers.bin', 'rb') as f:
    data = f.read()
    # Печатаем числа на экране
    for i in range(0, len(data), num_size):
        number = struct.unpack('q', data[i:i+num_size])[0]
        print(number)
