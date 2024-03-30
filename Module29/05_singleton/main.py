from typing import Any, Callable
import functools


def singleton(cls) -> Callable:
    """Декоратор класса. Отвечает за реализацию синглтонов."""
    @functools.wraps(cls)
    def wrapper(*args, **kwargs) -> Any:
        if cls.__name__ in wrapper.__instances:
            return wrapper.__instances[cls.__name__]
        else:
            instance: Any = cls(*args, **kwargs)
            wrapper.__instances[cls.__name__] = instance
            return instance

    wrapper.__instances = dict()  # Первые инстансы будем хранить в словаре по имени класса
    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
