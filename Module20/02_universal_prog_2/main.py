from math import sqrt
from typing import Iterable, Any


def is_prime(number: int) -> bool:
    """
    Функция определяет, является ли число простым.
    :param number: Натуральное число.
    :return: True, если число простое. Иначе - False
    """
    if number == 0 or number == 1:
        return False

    for divisor in range(2, int(sqrt(number)) + 1):
        if number % divisor == 0:
            return False
    return True


def crypto(iter_object: Iterable) -> list[Any]:
    """
    Функция возвращает список элементов итерируемого объекта,
    у которых индекс - простое число.
    :param iter_object: Итерируемый объект.
    :return: Список элементов с простыми индексами.
    Не будем усложнять жизнь и для словарей будем возвращать ключи
    с простыми индексами.
    """
    return [
        element
        for index, element in enumerate(iter_object)
        if is_prime(index)
    ]


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))
