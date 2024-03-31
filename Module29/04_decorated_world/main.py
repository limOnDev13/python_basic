from typing import Callable, Any
import functools


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """
    Декоратор для декораторов, который позволяет принимать
    другим декораторам произвольные аргументы.
    :param decorator: Декорируемый декоратор
    :type decorator: Callable
    :return: Декорированный декоратор, который способен принимать произвольные аргументы
    :rtype: Callable
    """
    @functools.wraps(decorator)
    def wrapped_decorator(*args, **kwargs) -> Callable:
        print(f'Переданные арги и кварги в декоратор:\n{args}\n{kwargs}')
        return decorator
    return wrapped_decorator


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable) -> Callable:
    """
    Простой декоратор для тестирования
    :param func: Декорируемая функция
    :type func: Callable
    :return: func
    :rtype: Callable
    """
    return func


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
