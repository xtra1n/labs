from func import f


def right_rectangle_method(
        start_value: int, finish_value: int, n: float) -> float:
    """
    Метод правых треугольников
    """
    step = (finish_value - start_value) / n
    integral = step * \
        sum(f(start_value + (i + 1) * step) for i in range(n))
    return integral


def trapezoid_method(start_value: int, finish_value: int, n: float) -> float:
    """
    Метод трапеций
    """
    step = (finish_value - start_value) / n
    integral = (step / 2) * (f(start_value) + f(finish_value)) +\
        step * sum(f(start_value + i * step) for i in range(1, n))
    return integral
