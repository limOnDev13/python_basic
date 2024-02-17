from string import ascii_letters, printable
import random


def generate_text(input_file: str = 'text.txt'):
    """
    Так как в папке нет файла text.txt.
    :param input_file: Название (путь) файла, куда будет сохраняться текст.
    :return: Ничего.
    """
    text: str = ''.join([random.choice(printable)
                         for _ in range(random.randint(10, 100))])

    with open(input_file, 'w') as file:
        file.write(text)


def get_text(input_file: str = 'text.txt') -> str:
    """
    Функция возвращает текст из файла input_file.
    :param input_file: Название (путь) файла, в котором хранится текст.
    :return: Текст из файла.
    """
    in_file = open(input_file, 'r', encoding='utf-8')
    text: str = in_file.read()
    in_file.close()
    return text


def frequency_analysis(text: str, output_file: str = 'analysis.txt'):
    """
    Функция производит частотный анализ и сохраняет его в файл.
    :param text: Текст для анализа.
    :param output_file: Название (путь) файла, куда будет сохраняться результат.
    :return: Ничего.
    """
    # Соберем словарь частот букв
    result_dict: dict[str, int] = dict()

    for sym in text:
        if sym.lower() in result_dict:
            result_dict[sym.lower()] += 1
        elif sym in ascii_letters:
            result_dict[sym.lower()] = 1

    # Запишем результат согласно заданию
    total_num_syms: int = sum(list(result_dict.values()))

    with open(output_file, 'w') as file:
        # Отсортируем словарь согласно заданию
        sorted_list_res: list[tuple[str, int]] = sorted(list(result_dict.items()),
                                                        key=lambda x: (x[1], -ord(x[0])), reverse=True)

        for sym, num_syms in sorted_list_res:
            file.write('{letter} {frequency}\n'.format(
                letter=sym,
                frequency=round(num_syms / total_num_syms, 3)
            ))


# generate_text()
frequency_analysis(get_text())
