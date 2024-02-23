from random import randint
from service import servise


def total_num_letters(names: list[str], log_file: str = 'errors.log') -> int:
    """
    Функция считает общее количество букв в списке имен.
    :param names: Список имен.
    :param log_file: Имя (путь) файла для логов ошибок.
    :return: Количество букв.
    """
    result_num_letters: int = 0

    with open(log_file, 'w', encoding='utf-8') as file:
        for num_name, name in enumerate(names):
            try:
                result_num_letters += len(name)
                if len(name) < 3:
                    raise ValueError(f'Ошибка: менее трех символов в строке {num_name + 1}')
            except (ValueError, BaseException) as exc:
                file.write(f'{str(exc)}\n-----------------\n')

    return result_num_letters


# Сгенерируем файл people.txt
# servise.save_words(servise.generate_words(randint(1, 20)), 'people.txt')
names_list: list[str] = servise.read_words('people.txt')
print('Общее количество символов:', total_num_letters(names_list))
