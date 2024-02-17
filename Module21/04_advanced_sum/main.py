def new_sum(*args) -> int:
    """
    Функция складывает числа. Передается неопределенное количество чисел.
    Числа могут быть в списках (в том числе и вложенных).
    :param args: Числа или списки чисел.
    :return: Сумму переданных чисел.
    """
    result_sum: int = 0

    for arg in args:
        if isinstance(arg, list):
            for elem in arg:
                result_sum += new_sum(elem)
        else:
            result_sum += arg

    return result_sum


# print(new_sum([[1, 2, [3]], [1], 3]))
