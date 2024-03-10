from typing import Iterable


class SqrIterator:
    """
    Класс-итератор, который создает последовательность квадратов чисел.
    Args:
        limit (int) - предел чисел, для которых нужно считать квадраты.
    """
    def __init__(self, limit: int) -> None:
        self.__limit: int = limit
        self.__counter: int = 0

    def __iter__(self) -> 'SqrIterator':
        self.__counter = 0
        return self

    def __next__(self) -> int:
        if self.__counter >= self.__limit:
            raise StopIteration
        else:
            self.__counter += 1
            return self.__counter ** 2


def sqr_generator(limit: int) -> Iterable:
    """
    Метод - генератор для генерации квадратов чисел
    :param limit: Предел чисел, для которых нужно считать квадраты
    :type limit: int
    :return: Последовательность квадратов чисел
    :rtype: Iterable
    """
    number: int = 0

    while number < limit:
        number += 1
        yield number ** 2


nums_limit: int = 10
# С помощью итератора
print('С помощью итератора:')
for num in SqrIterator(nums_limit):
    print(num, end=' ')

# С помощью генератора
print('\nС помощью генератора:')
for num in sqr_generator(nums_limit):
    print(num, end=' ')

# С помощью генераторного выражения
print('\nС помощью генераторного выражения:')
for num in (num ** 2 for num in range(1, nums_limit + 1)):
    print(num, end=' ')
