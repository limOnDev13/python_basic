def read_input(in_file: str) -> int:
    """
    Функция считывает все числа из файла и возвращает их сумму.
    :param in_file: Название файла (или абсолютный путь до него).
    :return: Сумму чисел, считанных из файла.
    """
    list_nums: list[str] = list()

    with open(in_file, 'r', encoding='utf-8') as file:
        for line in file:
            list_nums.extend(line.rstrip('\n').split())

    return sum([int(num) for num in list_nums])


def save_result(data: int, out_file: str):
    """
    Функция сохраняет в файл out_file переданное число data.
    :param data: Целое число, которое необходимо сохранить.
    :param out_file: Название (или абсолютный путь) файла, в который
    будет сохраняться data. Файл будет каждый раз перезаписываться.
    :return: Ничего
    """
    with open(out_file, 'w') as file:
        file.write(str(data))


save_result(read_input('numbers.txt'), 'answer.txt')
