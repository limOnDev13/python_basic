from typing import Callable


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор. Перед выполнением любой функции спрашивает как дела и в независимости от ответа пишет в консоль
    'А у меня не очень! Ладно, держи свою функцию.'
    :param func: Оборачиваемая функция
    :type func: Callable
    :return: func без изменений
    :rtype: Callable
    """
    input('Как дела? ')
    print('А у меня не очень! Ладно, держи свою функцию.')
    return func


@how_are_you
def test() -> None:
    """Тестовая функция"""
    print('<Тут что-то происходит...>')


test()
