import functools
from typing import Callable, Any
import time
from service.servise import timer


def slow_motion(seconds: int = 1) -> Callable:
    """
    Декоратор. Перед выполнением переданной функции ожидает seconds сек.
    :param seconds: Количество секунд для ожидания
    :type seconds: int
    :return: Обернутую функцию
    :rtype: Callable
    """
    def decorator(func: Callable) -> Callable:
        """
        Функция для декорирования.
        На самом деле я посмотрел на stackoverflow как передать аргумент декоратору
        и не совсем понимаю как это работает.
        :param func: Оборачиваемая функция
        :type func: Callable
        :return: func без изменений
        :rtype: Callable
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            """
            Обертка для func
            :return: результат работы func
            :rtype: Any
            """
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@timer
@slow_motion(3)
def test(x: int) -> None:
    """
    Функция для тестирования декоратора
    :return: None
    """
    print('Тестовая функция')


test(1)
