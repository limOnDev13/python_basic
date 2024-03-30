import functools
from typing import Callable, Any, Optional


USER_PERMISSIONS: list[str] = ['admin']


def check_permission(user_name: str) -> Callable:
    """
    Декоратор с аргументом. Проверяет права доступа
    :param user_name: Имя пользователя
    :type user_name: str
    :return: Обернутый декоратор
    :rtype: Callable
    """
    def decorator(func: Callable) -> Callable:
        """Обертка для функции"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Optional[Any]:
            if user_name in USER_PERMISSIONS:
                return func(*args, **kwargs)
            else:
                print('У пользователя {name} недостаточно прав, чтобы выполнить функцию {func_name}'.format(
                    name=user_name,
                    func_name=func.__name__
                ))
                return None
        return wrapper
    return decorator


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
