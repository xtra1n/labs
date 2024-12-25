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
    print('task1(Удалить нечетные): ', end='')
    read_file()
    print('\n')

    create_file()
    add_doubled_values(file)
    print('task2(Удвоенное четное): ', end='')
    read_file()
    print('\n')

    create_file()
    binary_insertion_sort(file)
    print('task3(Бинарная вставка): ', end='')
    read_file()
    print('\n')

    


if __name__ == '__main__':
    main()