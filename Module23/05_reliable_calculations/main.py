import math
from typing import Any, SupportsFloat


def get_sage_sqrt(num: Any) -> float:
    """
    Функция выполняет безопасное извлечение квадратного корня.
    :param num: Число.
    :return: Квадратный корень.
    """
    try:
        if not isinstance(num, SupportsFloat):
            raise TypeError(f'{num} не является типом,'
                            f' из которого можно извлечь квадратный корень')
        elif num < 0:
            raise ValueError(f'{num} меньше 0!')
        return math.sqrt(num)
    except (TypeError, ValueError) as exc:
        print(exc)
    except Exception:
        print('Непредвиденная ошибка!')



# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")
