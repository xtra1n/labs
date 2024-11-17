from utils import get_user_input, output_results
from integrals import right_rectangle_method, trapezoid_method
from func import F


def compute_integrals(start_value, finish_value, n1, n2):
    i1 = right_rectangle_method(start_value, finish_value, n1)
    i2 = right_rectangle_method(start_value, finish_value, n2)
    i3 = trapezoid_method(start_value, finish_value, n1)
    i4 = trapezoid_method(start_value, finish_value, n2)
    return i1, i2, i3, i4


def compute_errors(i1, i2, i3, i4, exact_value):
    abs_error_i1 = abs(i1 - exact_value)
    abs_error_i2 = abs(i2 - exact_value)
    abs_error_i3 = abs(i3 - exact_value)
    abs_error_i4 = abs(i4 - exact_value)

    relative_error_i1 = abs(i1 - exact_value) / abs(exact_value)
    relative_error_i2 = abs(i2 - exact_value) / abs(exact_value)
    relative_error_i3 = abs(i3 - exact_value) / abs(exact_value)
    relative_error_i4 = abs(i4 - exact_value) / abs(exact_value)

    return (abs_error_i1, abs_error_i2, abs_error_i3, abs_error_i4,
            relative_error_i1, relative_error_i2,
            relative_error_i3, relative_error_i4)


def find_min(err1, err2, err3, err4):
    return (err1 < err2 and err1 < err3 and
            err1 < err4)


def compute_accurate_value(abs_error_i1, abs_error_i2,
                           abs_error_i3, abs_error_i4):
    if find_min(abs_error_i1):
        accurate_value = abs_error_i1
        accurate_method = 1
    elif find_min(abs_error_i2):
        accurate_value = abs_error_i2
        accurate_method = 1
    elif find_min(abs_error_i3):
        accurate_value = abs_error_i3
        accurate_method = 2
    else:
        accurate_value = abs_error_i4
        accurate_method = 2

    return accurate_value, accurate_method


def main():
    start_value, finish_value, n1, n2 = get_user_input()
    i1, i2, i3, i4 = compute_integrals(start_value, finish_value, n1, n2)

    exact_value = F(finish_value) - F(start_value)
    abs_error_i1, abs_error_i2, abs_error_i3, abs_error_i4, \
        relative_error_i1, relative_error_i2, \
        relative_error_i3, relative_error_i4 = \
        compute_errors(i1, i2, i3, i4, exact_value)

    output_results(i1, i2, i3, i4, n1, n2)

    print('\nТаблица абсолютных погрешностей:\n')
    output_results(abs_error_i1, abs_error_i2,
                   abs_error_i3, abs_error_i4, n1, n2)

    print('\nТаблица относительных погрешностей:\n')
    output_results(relative_error_i1, relative_error_i2,
                   relative_error_i3, relative_error_i4, n1, n2)

    accurate_value, acurate_method = compute_accurate_value(
        abs_error_i1, abs_error_i2, abs_error_i3, abs_error_i4)

    print(f'Наиболее точное значение: {accurate_value},'
          f'найденное {acurate_method}-м способом')


if __name__ == '__main__':
    main()