from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор. Перед выполнением любой функции спрашивает как дела и в независимости от ответа пишет в консоль
    'А у меня не очень! Ладно, держи свою функцию.'
    :param func: Оборачиваемая функция
    :type func: Callable
    :return: func без изменений
    :rtype: Callable
    """
    def wrapper(*args, **kwargs) -> Any:
        """
        Обертка для func
        :return: Результат работы func
        :rtype: Any
        """
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        return func(*args, **kwargs)
    return wrapper


@how_are_you
def test(x: int) -> None:
    """Тестовая функция"""
    print('<Тут что-то происходит...>')


test(1)
