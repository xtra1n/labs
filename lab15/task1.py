import struct
import os

def remove_odd_numbers(file_name):
    record_size = struct.calcsize('i')
    with open(file_name, 'r+b') as f:
        pos = 0  # текущая позиция в файле
        byte = f.read(record_size)  # считываем первое число
        
        while byte:
            num = struct.unpack('i', byte)[0]  # распаковываем число
            
            if num % 2 == 0:  # если число четное
                # Если это четное число, перемещаем его в текущую позицию
                f.seek(pos)
                f.write(struct.pack('i', num))
                pos += 4  # двигаем позицию на 4 байта вперед
            # Если число нечетное, просто пропускаем его и не меняем позицию

            # Читаем следующее число
            byte = f.read(record_size)
        
        # После окончания обработки, заполняем оставшееся место нулями
        # для того чтобы удалить "старые" данные в конце файла
        f.truncate(pos)
