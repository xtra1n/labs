"""
Леонтьев Андрей ИУ7-14Б

Лабораторная работа №10 “Вычисление
приближённого значения интеграла”
Требуется написать программу для вычисления приближённого значения интеграла
известной, заданной в программе, функции двумя разными методами (по варианту).
Программа должна позволять задать начало и конец отрезка интегрирования, 
а также N1 и N2 - количества участков разбиения.
Далее построить таблицу следующего вида:

            N1 N2
    Метод 1 I1 I2
    Метод 2 I3 I4

Далее на основе известной, заданной в программе, первообразной определить, 
какой метод является наиболее точным. Для этого требуется вычислить и 
отобразить абсолютную и относительную погрешности каждого из четырёх измерений.
Метод, измерение которого с одним из разбиений дало самое близкое
первообразной значение, считается наиболее точным.
Затем для другого, менее точного метода, итерационно вычислить количество 
участков разбиения, для которого интеграл будет вычислен с заданной точностью, 
на основе формулы:
    𝐼(𝑁) − 𝐼(2𝑁)| | < ε
Вывести приближенное значение интеграла и количество отрезков, необходимых для
его вычисления.
"""


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
