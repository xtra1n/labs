from integrals import right_rectangle_method, trapezoid_method


def compute_integrals(start_value, finish_value, n1, n2):
    """
    Нахождение интеграла
    """
    i1 = right_rectangle_method(start_value, finish_value, n1)
    i2 = right_rectangle_method(start_value, finish_value, n2)
    i3 = trapezoid_method(start_value, finish_value, n1)
    i4 = trapezoid_method(start_value, finish_value, n2)
    return i1, i2, i3, i4


def compute_errors(i1, i2, i3, i4, exact_value):
    """
    Нахождение погрешностей
    """
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
    """
    Поиск минимального
    """
    return (err1 < err2 and err1 < err3 and
            err1 < err4)


def compute_accurate_value(abs_error_i1, abs_error_i2,
                           abs_error_i3, abs_error_i4):
    """
    Поиск минимальной погрешности
    """
    if find_min(abs_error_i1, abs_error_i2,
                abs_error_i3, abs_error_i4):
        accurate_value = abs_error_i1
        accurate_method = 1
    elif find_min(abs_error_i2, abs_error_i1,
                  abs_error_i3, abs_error_i4):
        accurate_value = abs_error_i2
        accurate_method = 1
    elif find_min(abs_error_i3, abs_error_i2,
                  abs_error_i1, abs_error_i4):
        accurate_value = abs_error_i3
        accurate_method = 2
    else:
        accurate_value = abs_error_i4
        accurate_method = 2

    return accurate_value, accurate_method


def compute_n(acurate_method, start_value, finish_value, eps):
    """
    Нахождение количества участков для менее точного метода
    """
    n = 1
    method = (right_rectangle_method if acurate_method == 2
              else trapezoid_method)
    while abs(method(start_value, finish_value, n) -
              method(start_value, finish_value, 2*n)) >= eps:
        n += 1000

    return n
