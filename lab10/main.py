from utils import get_user_input, output_results
from compute_utils import compute_integrals, compute_errors, \
      compute_accurate_value
from func import F


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
