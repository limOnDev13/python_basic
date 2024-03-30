from typing import Callable, Any
import functools


app: dict[str, Callable] = dict()


def callback(key: str) -> Callable:
    """
    Метод - декоратор с аргументом. Добавляет в словарь по ключу методы.
    :raise KeyError: Если методы имеют одинаковые ключи
    :param key: Ключ, по которым методы будут храниться в словаре app
    :type key: str
    :return: Ту же самую функцию без изменений
    :rtype: Callable
    """
    def callback_decorator(func: Callable) -> Callable:
        """Декоратор"""
        if key in app:
            raise KeyError('По ключу {key} уже хранится метод {func}'.format(
                key=key,
                func=app[key].__name__
            ))
        app[key] = func
        return func
    return callback_decorator


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


print(app)
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
