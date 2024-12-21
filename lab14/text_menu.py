from utils import get_path, init_db, output_bd, add_record, remove_record, get_position,\
                  search_one_field, search_two_fields

def print_menu():
    print('\n 1.Выбрать файл для работы\n',
            '2.Инициализировать базу данных\n',
            '3.Вывести содержимое базы данных\n',
            '4.Добавить запись в произвольное место базы данных\n',
            '5.Удалить произвольную запись из базы данных\n',
            '6.Поиск по одному полю\n',
            '7.Поиск по двум полям\n')
    
def menu():
    print_menu()

    path = None

    while True:
        try:
            point = int(input('\nВыберите пункт меню: '))
            if point == 1:
                path = get_path()
            elif path is not None:
                if point == 2:
                    init_db(path)
                    print_menu()
                elif point == 3:
                    output_bd(path)
                    print_menu()
                elif point == 4:
                    position = get_position()
                    add_record(path, position)
                    print_menu()
                elif point == 5:
                    position = get_position()
                    remove_record(path, position)
                    print_menu()
                elif point == 6:
                    search_one_field(path)
                    print_menu()
                elif point == 7:
                    search_two_fields(path)
                    print_menu()
                elif point == 0:
                    break
                else:
                    raise ValueError('Неверный пункт меню')
            elif path is None:
                print('Выберите файл для работы')
                print_menu()
        except ValueError:
            print('\nНекорректный пункт меню\n')
            print_menu()
        except Exception as e:
            print('Ой!', e, '\n')
            print_menu()