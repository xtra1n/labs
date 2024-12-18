from prettytable import PrettyTable


def search_by_two_fields(path):
    smth_searched = False
    try:
        record_1_1, record_1_2 = map(int, input('Введите диапазон для поиска по uder_id: ').split())
        record_2 = input('Введите поле для поиска по username: ')
        output = PrettyTable()
        with open(path, 'r') as file:
            output.field_names = file.readline().strip().split('|')
            for line in file:
                if int(line.strip().split('|')[0]) in range(record_1_1, record_1_2 + 1) and\
                    record_2 in line.strip().split('|')[1]:
                    output.add_row(line.strip().split('|'))
                    smth_searched = True
            if smth_searched is False:
                print('Ничего не нашлось')
        if smth_searched is True:
            print(output)
    except Exception as e:
        print('Ой!', e)


def output_bd(path):
    output = PrettyTable()
    with open(path, 'r') as file:
        print()
        output.field_names = file.readline().strip().split('|')
        for line in file:
            output.add_row(line.strip().split('|'))
        print(output)


def main():
    path = '../bd'
    while True:
        output_bd(path)
        search_by_two_fields(path)


if __name__ == '__main__':
    main()