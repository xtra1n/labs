from os import getcwd
from os.path import exists
from prettytable import PrettyTable

def get_path():

    cur_dir = getcwd()

    print(f'\nТекущая дирректория: {cur_dir}\n')

    path = input('Введите путь к файлу: ')

    return path


def init_db(path):
    try:
        with open(path, 'w') as file:
            file.write('user_id|username|email|status\n')
            print('База данных инициализирована успешна')
    except Exception:
        raise FileNotFoundError('Не удалось инициализировать базу данных')
    

def output_bd(path):
    check_file(path)
    output = PrettyTable()
    with open(path, 'r') as file:
        info = file.readline().strip().split('|')
        # pretty_output = '=' * len(info)
        print()
        # print(pretty_output, end='')
        output.field_names  = info
        # print(f'\n{info}')
        for line in file:
            output.add_row(line.strip().split('|'))
        print(output)

def add_record(path):
    check_file(path)
    with open(path, 'a') as file:
        record = get_record(path)
        file.write(record + '\n')

    print('Запись добавлена')

def get_record(path):
    try:
        user_id = get_user_id(path)
        username = get_username()
        email = get_email()
        status = get_status()

        return f'{user_id}|{username}|{email}|{status}'

    except Exception as e:
        print(e)
    

def get_user_id(path):
    max_id = 0
    with open(path, 'r') as file:
        for line in file:
            record = line.strip().split('|')
            if record[0].isnumeric():
                max_id = max(max_id, int(record[0]))
    return max_id + 1


def get_username():
    try:
        username = input('Введите имя пользователя: ')
        if username.isnumeric() or len(username) == 0 \
            or (not(username.isalnum())):
            raise ValueError('Некорректное имя пользователя')
        elif '|' in username:
            raise ValueError('Данные не могут содержаться символ "|"')
        else:
            return username
    except Exception as e:
        print('Ой!', e)
        return get_username()
        

def get_email():
    try:
        email = input('Введите email: ')
        if (('@' not in email) or ('.' not in email) or
            email.index('@') > email.rindex('.') or len(email) < 5 or \
            (not(email[0].isalnum())) or (not(email[-1].isalnum())) or \
            '@.' in email or \
                '.@' in email or email.count('@') != 1 or email.count('.') != 1):
            raise ValueError('Некорректный email')
        elif '|' in email:
            raise ValueError('Данные не могут содержаться символ "|"')
        else:
            return email
    except Exception as e:
        print('Ой!', e)
        return get_email()


def get_status():
    try:
        status = int(input('Введите статус пользователя( 1.active / 2.banned): '))
        if status != 1 and status != 2:
            raise ValueError('Неверный status пользователя')
        elif status == 1:
            return 'active'
        else:
            return 'banned'
    except Exception as e:
        print('Ой!', e)
        return get_status()


def search_one_field(path):
    check_file(path)
    recrod = input('Введите запись для поиска в поле email: ')
    output = PrettyTable()
    with open(path, 'r') as file:
        output.field_names = file.readline().strip().split('|')
        file.readline()
        smth_searched = False
        print('\nНайденные записи:')
        for line in file:
            if line.split('|')[2] == recrod:
                print(line.strip())
                output.add_row(line.strip().split('|'))
                smth_searched = True
        if smth_searched is False:
            print('Ничего не нашлось')
    if smth_searched is True:
        print(output)


def search_two_fields(path):
    check_file(path)
    record_1 = input('Введите запись для поиска в поле username: ')
    record_2 = input('Введите запись для поиска в поле status: ')
    output = PrettyTable()
    with open(path, 'r') as file:
        output.field_names = file.readline().strip().split('|')
        smth_searched = False
        print('\nНайденный записи: ')
        for line in file:
            if line.strip().split('|')[1] == record_1 and \
                line.strip().split('|')[3] == record_2:
                output.add_row(line.strip().split('|'))
                smth_searched = True
        if smth_searched is False:
            print('\nНичего не нашлось')
    if smth_searched is True:
        print(output)

def check_file(path):
    if not exists(path):
        raise FileNotFoundError('Неверный путь к базе данных')
