from utils import get_user_input, output_results, get_float_input
from compute_utils import compute_integrals, compute_errors, \
      compute_accurate_value, compute_n
from func import F
from integrals import right_rectangle_method, trapezoid_method


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

    print(f'Наиболее маленькая абс. погрешность: {accurate_value:.6g},'
          f'найдена {acurate_method}-м способом')

    eps = get_float_input('Введите значение для e: ')

    n = compute_n(acurate_method, start_value, finish_value, eps)
    print(f'Количество участков с точностью {eps: .5g}: {n}')

    if acurate_method == 1:
        new_value = trapezoid_method(start_value, finish_value, n)

    else:
        new_value = right_rectangle_method(start_value, finish_value, n)

    print(f'\nПриближенное значение интеграла : {new_value:.10f}')
    print(f'Которое удалось вычислить за кол-во отрезков {n}')


if __name__ == '__main__':
    main()
