from typing import Callable, Any
from time import time


class LoggerDecorator:
    def __init__(self, func: Callable) -> None:
        self.__func: Callable = func
        self.__start: float = time()

    def __call__(self, *args, **kwargs) -> Any:
        res: Any = self.__func(*args, **kwargs)

        print('\n--------------------------------\n'
              'Функция {func}:\n'
              'Аргументы:\n\targs: {arg}\n\tkwargs: {kwarg}\n'
              'Время выполнения: {time}s'.format(
                func=self.__func.__name__,
                arg=args,
                kwarg=kwargs,
                time=time() - self.__start
              ))
        return res


@LoggerDecorator
def complex_algorithm(arg1, arg2):
    # Здесь выполняется сложный алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result


# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)