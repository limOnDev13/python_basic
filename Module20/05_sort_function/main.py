# from random import randint
from typing import Any


def qsort(list_nums: list[int], reverse: bool = False) -> list[int]:
    """
    Функция быстрой сортировки (опорный элемент - 0-й)
    с помощью рекурсии.
    :param list_nums: Список чисел.
    :param reverse: Параметр показывает в какую сторону сортировать.
    Если False - по возрастанию, True - по убыванию.
    :return: Отсортированный список.
    """
    # Если получен список из одного элемента или пустой -
    # условие остановки рекурсии
    if len(list_nums) <= 1:
        return list_nums

    # Разбрасываем элементы по спискам
    # (элементы меньше опорного, равные ему и больше его)
    support_element: int = list_nums[0]
    small_nums: list[int] = [
        num
        for num in list_nums if num < support_element
    ]
    equal_nums: list[int] = [
        num
        for num in list_nums if num == support_element
    ]
    big_nums: list[int] = [
        num
        for num in list_nums if num > support_element
    ]

    # Собираем результат с помощью вспомогательного списка
    # и возвращаем его
    result_list: list[int] = list()
    if not reverse:
        result_list.extend(qsort(small_nums))
        result_list.extend(equal_nums)
        result_list.extend(qsort(big_nums))
    else:
        result_list.extend(qsort(big_nums))
        result_list.extend(equal_nums)
        result_list.extend(qsort(small_nums))
    return result_list


def tpl_sort(in_tuple: tuple[Any, ...],
             reverse: bool = False) -> tuple[Any, ...]:
    """
    Функция производит быструю сортировку для кортежа.
    :param in_tuple: Входной кортеж.
    :param reverse: Параметр показывает в какую сторону сортировать.
    Если False - по возрастанию, True - по убыванию.
    :return: Отсортированный кортеж.
    """
    # Проверим, что все элементы - целые числа
    for elem in in_tuple:
        if not isinstance(elem, int):
            return in_tuple

    temp_list: list[int] = qsort(list(in_tuple), reverse=reverse)
    return tuple(temp_list)


# tpl = (6, 3, -1, 8, 4, 10, -5)
# print(tpl_sort(tpl))
# numbers: tuple[int, ...] = tuple([randint(-100, 100)
#                                   for _ in range(randint(10, 50))])
# print(tpl_sort(numbers))
