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


def sof_counter(func: Callable) -> Callable:
    """
    Декоратор - счетчик вызовов декорируемой функции. Решение подсмотрено на StackOverFlow,
    есть пара непонятных моментов
    :param func: Декорируемая функция
    :type func: Callable
    :return: обернутую func
    :rtype: Callable
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """Обертка для func"""
        wrapper.__count += 1
        return func(*args, **kwargs)

    wrapper.__count: int = 0  # Почему-то pycharm ругается на аннотацию.
    # Пишет Non-self attribute could not be type hinted - непонятно...
    return wrapper


@sof_counter
@counter
def test1() -> None:
    """Тестовая функция"""
    pass


@sof_counter
@counter
def test2() -> None:
    """Тестовая функция"""
    pass


test1()
test1()
test2()
test2()
test2()
print(f'test1.__count = {test1.__count}')
print(f'test2.__count = {test2.__count}')  # А здесь ругается, что Cannot find reference '__count' in '(...) -> Any'
