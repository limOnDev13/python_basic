from typing import Callable, Any
import functools


COUNT_FUNCS: dict[str, int] = dict()


def counter(func: Callable) -> Callable:
    """
    Декоратор. Считает количество вызовов декорируемой функции
    :param func: Декорируемая функция
    :type func: Callable
    :return: func
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """Обертка для func"""
        if func.__name__ in COUNT_FUNCS:
            COUNT_FUNCS[func.__name__] += 1
        else:
            COUNT_FUNCS[func.__name__] = 1
        print('Функция {name} была вызвана {times} раз(а)'.format(
            name=func.__name__,
            times=COUNT_FUNCS[func.__name__]
        ))
        return func(*args, **kwargs)
    return wrapper


@counter
def test1() -> None:
    """Тестовая функция"""
    pass


@counter
def test2() -> None:
    """Тестовая функция"""
    pass


test1()
test1()
test2()
test2()
test2()
