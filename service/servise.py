import random
from string import ascii_lowercase, ascii_uppercase
from typing import Literal, Callable


def generate_words(number_words: int,
                   first_is_upper: bool = True,) -> list[str]:
    """
    Функция генерирует список случайных слов.
    :param number_words: Количество слов, которые нужно сгенерировать.
    :param first_is_upper: Параметр, который говорит,
    нужно ли делать первую букву заглавной. Если True - нужно.
    :return: Список сгенерированных слов.
    """
    return [
        ''.join([(random.choice(ascii_uppercase) if first_is_upper and num_let == 0 else
                  random.choice(ascii_lowercase))
                 for num_let in range(random.randint(1, 10))])
        for _ in range(number_words)
    ]


def generate_word(first_is_upper: bool = True) -> str:
    """
    Генерирует одно слово.
    :param first_is_upper: Если True - первая буква заглавная, иначе - строчная
    :return: Сгенерированное слово.
    """
    return ''.join([
        (random.choice(ascii_uppercase) if first_is_upper and num_let == 0 else
         random.choice(ascii_lowercase))
        for num_let in range(random.randint(1, 10))
    ])


def save_words(words: list[str], file_name: str,
               mode: Literal['w', 'a', 'x'] = 'w', sep: str = '\n'):
    """
    Функция сохраняет список слов с разделителем в файл.
    :param words: Список слов.
    :param file_name: Название (путь) файла с результатом.
    :param mode: Режим записи.
    :param sep: Разделитель слов.
    :return: Ничего
    """
    with open(file_name, mode, encoding='utf-8') as file:
        file.write(sep.join(words))


def read_words(input_file: str) -> list[str]:
    """
    Функция считывает из файла данные, которые записаны в строки.
    :param input_file: Имя (путь) файла с данными.
    :return: Список считанных строк.
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        return file.read().split('\n')


def logging(log_file: str) -> Callable:
    """
    Функция - обертка для логирования. Будет отлавливать ValueError,
    связанный с логической ошибкой в решении задачи.
    :param log_file: Название (путь) файла, в который будут записываться исключения.
    :return: Обернутую функцию.
    """
    def logging_decorator(func: Callable) -> Callable:
        def __wrapper(*args, **kwargs):
            with open(log_file, 'w', encoding='utf-8') as file:
                try:
                    func(*args, **kwargs)
                except ValueError as exc:
                    file.write(str(exc) + '\n\n')
        return __wrapper
    return logging_decorator


def create_file(file_name: str):
    """
    Функция создает файл.
    :param file_name: Имя файла.
    :return: Ничего.
    """
    try:
        with open(file_name, 'x', encoding='utf-8') as file:
            return
    except FileExistsError:
        return
