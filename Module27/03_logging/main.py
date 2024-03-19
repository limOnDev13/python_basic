from typing import Any, Callable
import functools
from datetime import datetime


LOG_FILE: str = 'function_errors.log'


def logging(func: Callable) -> Callable:
    """
    Декоратор для логгирования. Выводит на экран название функции и ее документацию.
    Если возникли ошибки - сохраняется дата - время ошибки, название функции, в которой возникло исключение
    и текст исключения.
    :param func: Логгируемая функция
    :type func: Callable
    :return: обертку func
    :rtype: Callable
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """Обертка для func"""
        print('Функция {name}:\n{line}\n{doc}\n{line}\n'.format(
            name=func.__name__,
            doc=func.__doc__,
            line='-' * 20
        ))

        try:
            return func(*args, **kwargs)
        except Exception as exc:
            # Запишем дату-время ошибки, имя функции, в которой вышло исключение и текст исключения
            with open(LOG_FILE, 'a', encoding='utf-8') as log_file:
                log_file.write('{date_time}: {func_name} - {error}\n{line}\n'.format(
                    date_time=datetime.now(),
                    func_name=func.__name__,
                    error=exc,
                    line='-' * 20
                ))
            return None
    return wrapper


@logging
def test_func1() -> None:
    """Тестовая функция без ошибок"""
    print('Функция без ошибок')


@logging
def test_func2() -> None:
    """
    Тестовая функция с ошибкой
    :return: None
    """
    print(aaa)


@logging
def test_func3() -> None:
    """Тестовая функция с ошибкой"""
    print(1 / 0)


test_func1()
test_func2()
test_func3()
test_func3()
test_func3()
test_func3()
