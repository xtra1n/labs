from struct import calcsize, pack, unpack
from os import getcwd, SEEK_CUR, SEEK_END
from os.path import exists
from prettytable import PrettyTable


RECORD_FORMAT = 'i20s20si'
RECORD_SIZE = calcsize(RECORD_FORMAT)


def pack_data(user_id: int, username: str, email:str, status: int):
    username = username.encode('utf-8')
    email = email.encode('utf-8')
    packed_data = pack(RECORD_FORMAT, user_id, username, email, status)
    
    return packed_data

def get_path():

    cur_dir = getcwd()

    print(f'\nТекущая дирректория: {cur_dir}\n')

    path = input('Введите путь к файлу: ')

    return path


def init_db(path):
    try:
        with open(path, 'wb') as file:
            print('База данных инициализирована успешна')
    except Exception:
        raise FileNotFoundError('Не удалось инициализировать базу данных')
    

def output_bd(path):
    check_file(path)
    print()
    output = PrettyTable()
    output.field_names  = (['user_id', 'username', 'email', 'status '])
    with open(path, 'rb') as file:
        while chunk := file.read(RECORD_SIZE):
            user_id, username, email, status = list(unpack(RECORD_FORMAT, chunk))
            username = username.decode('utf-8').rstrip("\x00")
            email = email.decode('utf-8').rstrip("\x00")
            output.add_row([user_id, username, email, status])
        print(output)


def add_record(path, position):
    check_file(path)
    with open(path, 'rb+') as file:
        record = get_record(path)
        file.read(position * RECORD_SIZE)
        while line := file.read(RECORD_SIZE):
            file.seek(-RECORD_SIZE, SEEK_CUR)
            file.write(record)
            record = line
        file.write(record)
    print('Запись добавлена')

def get_record(path):
    try:
        user_id = get_user_id(path)
        username = get_username()
        email = get_email()
        status = get_status()

        record = pack_data(user_id, username, email, status)

        return record

    except Exception as e:
        print(e)
    

def get_user_id(path):
    max_id = 0
    with open(path, 'rb') as file:
        while line := file.read(RECORD_SIZE):
            user_id, _, _, _ = unpack(RECORD_FORMAT, line)
            max_id = max(max_id, int(user_id))
    return max_id + 1


def get_username():
    try:
        username = input('Введите имя пользователя: ')
        if username.isnumeric() or len(username) == 0 \
            or (not(username.isalnum())):
            raise ValueError('Некорректное имя пользователя')
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
            return 1
        else:
            return 2
    except Exception as e:
        print('Ой!', e)
        return get_status()

def remove_record(path, position):
    check_file(path)
    with open(path,     'r+b') as file:
        file.read(position * RECORD_SIZE)
        while file.read(RECORD_SIZE) and (next_line := file.read(RECORD_SIZE)):
            file.seek(-2 * RECORD_SIZE, SEEK_CUR)
            file.write(next_line)
        file.seek(-RECORD_SIZE, SEEK_END)
        file.truncate()

def search_one_field(path):
    check_file(path)
    record = input('Введите запись для поиска в поле email: ')
    output = PrettyTable()
    print('\nНайденные записи:')
    output.field_names = ['user_id', 'username', 'email', 'status']
    with open(path, 'rb') as file:
        smth_searched = False
        while chunk := file.read(RECORD_SIZE):
            user_id, username, email, status = list(unpack(RECORD_FORMAT, chunk))
            email = email.decode('utf-8').rstrip("\x00")
            if email == record:
                username = username.decode('utf-8').rstrip('\x00')
                output.add_row([user_id, username, email, status])
                smth_searched = True
        if smth_searched is False:
            print('Ничего не нашлось')
    if smth_searched is True:
        print(output)


def search_two_fields(path):
    try:
        check_file(path)
        record_1 = input('Введите запись для поиска в поле username: ')
        record_2 = int(input('Введите запись для поиска в поле status: '))
        output = PrettyTable()
        print('\nНайденные записи:')
        output.field_names = ['user_id', 'username', 'email', 'status']
        with open(path, 'rb') as file:
            smth_searched = False
            while chunk := file.read(RECORD_SIZE):
                user_id, username, email, status = list(unpack(RECORD_FORMAT, chunk))
                username = username.decode('utf-8').rstrip("\x00")
                if username == record_1 and status == record_2:
                    email = email.decode('utf-8').rstrip('\x00')
                    output.add_row([user_id, username, email, status])
                    smth_searched = True
            if smth_searched is False:
                print('Ничего не нашлось')
        if smth_searched is True:
            print(output)
    except Exception as e:
        print('Ой!', e)
        return search_two_fields()

def check_file(path):
    if not exists(path):
        raise FileNotFoundError('Неверный путь к базе данных')
    
def get_position():
    try:
        position = int(input('Введите номер позиции: '))
        if position < 0:
            raise ValueError('Неверный номер позиции (< 0)')
        else:
            return position
    except Exception as e:
        print('Ой!', e)
        return get_position()