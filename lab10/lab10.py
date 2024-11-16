def get_user_input():
    while True:
        try:
            start_value = float(input('Введите начальное значение: '))
            finish_value = float(input('Введите конечное значение: '))

            if start_value > finish_value:
                raise ValueError('Начальное значение должно быть меньше конечного')

            n1 = int(input('Введите количество участков разбиения №1: '))
            n2 = int(input('Введите количество участков разбиения №2: '))

            if n1 <= 0 or n2 <= 0:
                raise ValueError('Количество участков разбиения должно быть положительным')

            return start_value, finish_value, n1, n2
        except ValueError as e:
            print(f'Ой! {e}')



def main():
    start_value, finish_value, n1, n2 = get_user_input()
    print(n1, n2, start_value, finish_value)

if __name__ == '__main__':
    main()