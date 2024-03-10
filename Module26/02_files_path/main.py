import os
from typing import Iterable


def gen_files_path(required_file: str,
                   init_dir: str = os.path.abspath(os.path.sep)) -> Iterable:
    """
    Генератор для получения всех файлов, встреченных во время поиска необходимого файла
    :raise ValueError: Выбрасывает, если файл не найден.
    :param required_file: Название файла (или директории), который нужно найти
    :type required_file: str
    :param init_dir: Название директории, в которой нужно искать required_file
    :type init_dir: str
    :return: Встреченные файлы
    :rtype: Iterable
    """
    dir_tree: Iterable = os.walk(init_dir)

    for root, dirs, files in dir_tree:
        if required_file in dirs or required_file in files:
            yield os.path.join(root, required_file)
            return
        else:
            for file in files:
                yield os.path.join(root, file)
    else:
        raise ValueError(f'Файл {required_file} в директории {init_dir} не найден!')


for file_name in gen_files_path(
        init_dir=os.path.abspath(os.path.join('..', '..')),
        required_file='02_files_path'):
    print(file_name)
