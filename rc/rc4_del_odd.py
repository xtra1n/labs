import struct

def remove_even_numbers_inplace(file_path):  # Переименовал параметр
    n = [9, 23, 121, 64, 1, 0, -10]
    with open(file_path, 'w+b') as file:  # Здесь всё нормально
        for i in n:
            record = struct.pack('q', i)
            file.write(record)
    
    with open(file_path, 'r+b') as f:  # Используем корректное имя
        read_pos = 0  # Позиция чтения
        write_pos = 0  # Позиция записи
        
        while True:
            f.seek(read_pos)  # Переходим к позиции чтения
            data = f.read(8)  # Читаем одно 8-байтовое число
            
            if not data:  # Если достигли конца файла, выходим из цикла
                break
            
            number = struct.unpack('q', data)[0]  # Распаковываем число
            
            if number % 2 != 0:  # Если число нечётное
                f.seek(write_pos)  # Переходим к позиции записи
                f.write(data)  # Записываем число
                write_pos += 8  # Смещаем позицию записи
            
            read_pos += 8  # Смещаем позицию чтения
        
        # Обрезаем файл, чтобы удалить остаток (чётные числа)
        f.truncate(write_pos)

    with open('numbers.bin', 'rb') as file:
        while line := file.read(8):
            line = struct.unpack('q', line)
            line = line[0]
            print(line)

# Пример вызова функции
remove_even_numbers_inplace('numbers.bin')
