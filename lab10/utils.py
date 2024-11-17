def get_user_input():
    while True:
        try:
            start_value = float(input('Введите начальное значение: '))
            finish_value = float(input('Введите конечное значение: '))

            if start_value > finish_value:
                raise ValueError(
                    'Начальное значение должно быть меньше конечного')

            n1 = int(input('Введите количество участков разбиения №1: '))
            n2 = int(input('Введите количество участков разбиения №2: '))

            if n1 <= 0 or n2 <= 0:
                raise ValueError(
                    'Количество участков разбиения должно быть положительным')

            return start_value, finish_value, n1, n2
        except ValueError as e:
            print(f'Ой! {e}')


def output_results(i1, i2, i3, i4, n1, n2):
    print('-' * 80)
    print('|', ' ' * 33, '|', f'{'N1: ' + f'{n1:.6g}': ^20}'
          f'|{'N2: ' + f'{n2:.6g}': ^20}|')
    print('-' * 80)
    print(f'|{'Метод правых прямоугольников':^35}|',
          f'{i1:^20.6g}|{i2:^20.6g}|')
    print('-' * 80)
    print(f'|{'Метод трапеций':^35}|', f'{i3:^20.6g}|{i4:^20.6g}|')
    print('-' * 80)