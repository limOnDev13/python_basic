from typing import Optional, Callable
import functools


def cash(func: Callable[[float | int], float | int]) -> Callable:
    """
    Декоратор. Кэширует результаты вычисления функции, которая принимает 1 числовой аргумент и возвращает также число
    :param func: Декорируемая функция
    :type func: Callable[[float | int], float | int]
    :return: Обертку для func
    :rtype: Callable
    """
    @functools.wraps(func)
    def cash_func(number: float | int) -> float | int:
        result: Optional[float | int] = cash_func.__cash.get(number)

        if result is None:
            result = func(number)
            cash_func.__cash[number] = result

        return result

    cash_func.__cash: dict[float | int, float | int] = dict()

    return cash_func


@cash
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован

# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован
print(fibonacci.__cash)
