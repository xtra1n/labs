import struct
import os

def add_doubled_values(file_name):
    record_size = struct.calcsize('i')
    # Открываем файл для чтения и записи
    with open(file_name, 'r+b') as f:
        # Чтение текущей позиции
        pos = 0
        
        while True:
            byte = f.read(record_size)  # Читаем 4 байта (одно 32-битное число)
            if not byte:
                break  # Достигнут конец файла
            
            num = struct.unpack('i', byte)[0]  # Распаковываем 32-битное число
            
            # Перемещаемся в нужную позицию для записи
            f.seek(pos)
            f.write(struct.pack('i', num))  # Записываем текущее число обратно в файл
            
            # Если число четное, добавляем его удвоенное значение
            if num % 2 == 0:
                # Перемещаемся в конец файла и записываем удвоенное значение
                f.write(struct.pack('i', num * 2))
            
            # Двигаем позицию на 4 байта вперед
            pos = f.tell()

        # Устанавливаем корректную длину файла, обрезая лишние данные (если они были)
        f.truncate(pos)
