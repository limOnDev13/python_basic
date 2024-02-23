import zipfile
from codecs import decode
from string import punctuation


def read_archive(archive: str = 'voyna-i-mir.zip',
                 file_name: str = 'voyna-i-mir.txt') -> str:
    """
    Функция считывает текст из файла file_name в архиве archive
    и возвращает его.
    :param archive: Название (путь) архива.
    :param file_name: Название (путь) файла, с которого нужно считать текст.
    :return: Текст из файла.
    """
    text: str

    with zipfile.ZipFile(archive) as arch:
        text = decode(arch.read(file_name))

    return text


def full_frequency_analysis(text: str) -> dict[str, float]:
    """
    Функция проводит полный частотный анализ (только по буквам) текста.
    :param text: Текст для анализа.
    :return: Словарь - частотный анализ букв.
    """
    # Чтобы не заморачиваться с французским алфавитом, будем включать
    # в словарь все символы, которые не являются знаками пунктуации.
    temp_dict: dict[str, int] = dict()  # Словарь с символами и их количествами

    for sym in text:
        if sym in temp_dict:
            temp_dict[sym] += 1
        elif sym not in punctuation + '0123456789– «»…„“—№°\n\t':
            temp_dict[sym] = 1

    total_num_syms: int = sum(list(temp_dict.values()))  # Общее кол-во букв

    return {
        key: round(value / total_num_syms, 5)
        for key, value in temp_dict.items()
    }


def save_result(frequencies: dict[str, float], reverse: bool = False,
                output_file: str = 'frequency_analysis.txt'):
    """
    Функция сохраняет частотный анализ в файл.
    :param frequencies: Словарь - частотный анализ.
    :param reverse: При сохранении будет сортировка. Если True - по убыванию, иначе - по возрастанию.
    :param output_file: Название (путь) файла, куда будет сохраняться результат.
    :return: Ничего.
    """
    # Отсортируем словарь (сказано только по частоте)
    sorted_dict: list[tuple[str, float]] = sorted(list(frequencies.items()),
                                                  key=lambda x: x[1] if reverse else -x[1])

    # Сохраним словарь в файл
    with open(output_file, 'w', encoding='utf-8') as file:
        for let, freq in sorted_dict:
            file.write('{letter}: {frequency}\n'.format(
                letter=let,
                frequency=freq
            ))


save_result(full_frequency_analysis(read_archive()))
