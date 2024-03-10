import random
from typing import Final


class KillError(Exception):
    """Класс-исключение (убийство)"""
    def __str__(self) -> str:
        return 'Убийство'


class DrunkError(Exception):
    """Класс-исключение (алкоголизм)"""
    def __str__(self) -> str:
        return 'Алкоголизм'


class CarCrashError(Exception):
    """Класс-исключение (ДТП)"""
    def __str__(self) -> str:
        return 'ДТП'


class GluttonyError(Exception):
    """Класс-исключение (обжорство)"""
    def __str__(self) -> str:
        return 'Обжорство'


class DepressionError(Exception):
    """Класс-исключение (депрессия)"""
    def __str__(self) -> str:
        return 'Депрессия'


def one_day() -> int:
    """
    Метод отвечает за один день жизни буддиста
    :raise KillError | DrunkError | CarCrashError | GluttonyError | DepressionError: ошибка выбрасывается
     с вероятностью 1 к 10.
    :return: Количество кармы за этот день
    :rtype: int
    """
    bad_chance: float = random.randint(1, 10)
    # Если не повезло, выкинем случайную ошибку
    if bad_chance == 1:
        raise random.choice((KillError, DrunkError, CarCrashError, GluttonyError, DepressionError))

    # Если повезло - вернем карму
    return random.randint(1, 7)


ENLIGHTENMENT: Final = 500


with open('karma.log', 'w', encoding='utf-8') as log_file:
    karma: int = 0
    count_days: int = 0
    while karma < ENLIGHTENMENT:
        try:
            karma += one_day()
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as exc:
            log_file.write('{day} день: {name} - {text}\n'.format(
                day=count_days,
                name=exc.__class__.__name__,
                text=str(exc)
            ))
        finally:
            count_days += 1
    print(f'Буддист достиг просветления за {count_days} дней.')
