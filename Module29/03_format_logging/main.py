from typing import Callable, Any, Optional
import functools
from datetime import datetime
from time import time


def example_format_to_right_format(pattern: str) -> str:
    """
    Метод приводит формат даты и времени из примера в правильный формат (для datetime),
    т.е. добавляет знак % Перед каждой буквой
    :param pattern: Формат даты и времени
    :type pattern: str
    :return: Правильный (для datetime) формат даты и времени
    :rtype: str
    """
    codes: str = 'aAbBcdHIjmMpSUwWxXyYZ%'
    right_format: str = ''

    for sym in pattern:
        if sym in codes:
            right_format += '%'
        right_format += sym

    return right_format


def logging(_func: Optional[Callable] = None, *, pattern: str, class_name: str) -> Callable:
    """
    Декоратор с аргументами. Логирует работу метода
    :param pattern: Формат записи даты и времени
    (b - месяц, d - день, Y - год, H - часы, M - минуты, S - секунды)
    :param _func: маркер
    :type _func: Optional[Callable]
    :type pattern: str
    :param class_name: Имя класса. Нужно для правильного вывода
    :type class_name: str
    :return: Функцию без изменений
    :rtype: Callable
    """
    def logging_decorator(func: Callable) -> Callable:
        """Обертка"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            print("- Запускается '{cls}.{func}'. Дата и время запуска: {date_time}".format(
                cls=class_name,
                func=func.__name__,
                date_time=datetime.now().strftime(example_format_to_right_format(pattern))
            ))
            start: float = time()
            result: Any = func(*args, **kwargs)
            print("- Завершение '{cls}.{func}', время работы = {time}s".format(
                cls=class_name,
                func=func.__name__,
                time=time() - start
            ))
            return result
        return wrapper
    if _func is None:
        return logging_decorator
    return logging_decorator(_func)


def log_methods(pattern: str) -> Callable:
    """
    Декоратор класса. Применяет декоратор @logging для всех немагических методов объекта класса.
    :param pattern: Формат даты и времени
    :type pattern: str
    :return: Метод без изменений
    :rtype: Callable
    """
    def decorate(cls):
        for i_method_name in dir(cls):
            if not i_method_name.startswith('__'):
                cur_method: Any = getattr(cls, i_method_name)

                decorated_method = logging(pattern=pattern, class_name=cls.__name__)(cur_method)
                setattr(cls, i_method_name, decorated_method)
        return cls
    return decorate


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj1 = B()
my_obj1.test_sum_1()
my_obj1.test_sum_2()
