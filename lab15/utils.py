import random
import struct

def create_file():
    arr = create_arr()

    print('Изначальная последовательность: ', end='')


    for el in arr:
        print(el, end=' ')
    
    print()

    with open('file.bin', 'wb') as file:
        for el in arr:
            file.write(struct.pack('i', el))

def create_arr():
    # Генерируем список случайных чисел
    n = random.randint(10, 20)  # Размер массива от 10 до 20
    arr = [random.randint(-100, 100) for _ in range(n)]  # Список случайных чисел от -100 до 100
    return arr

def read_file():
    with open('file.bin', 'rb') as file:
        print('Содержимое файла: ', end='')
        while el := file.read(4):
            print(struct.unpack('i', el)[0], end=' ')

