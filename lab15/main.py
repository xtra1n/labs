'''
Леонтьев Андрей
ИУ7-14Б
Лабараторная работа №14. 
'''


from task1 import remove_odd_numbers
from task2 import add_doubled_values
from task3 import binary_insertion_sort
from utils import create_file, read_file


def main():
    file = 'file.bin'
    create_file()
    remove_odd_numbers(file)
    print('task1: ', end='')
    read_file()
    print()

    create_file()
    add_doubled_values(file)
    print('task2: ', end='')
    read_file()
    print()

    create_file()
    binary_insertion_sort(file)
    print('task3: ', end='')
    read_file()
    print()

    


if __name__ == '__main__':
    main()