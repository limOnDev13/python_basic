import os
import re
from typing import Iterable, Iterator


def gen_num_strings(init_dir: str) -> Iterable:
    """
    Генератор для получения количеств строк во всех файлах .py в указанной директории.
    В расчет не берутся пустые строки и комментарии
    :param init_dir: Имя директории, в которой нужно искать файлы .py
    :type init_dir: str
    :return: Количества строк в каждом .py файле
    :rtype: Iterable
    """
    dir_tree: Iterator = os.walk(init_dir)

    for root, dirs, files in dir_tree:
        for file in files:
            if re.match(r".*\.py", file):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as py_file:
                    count_lines: int = 0
                    comment: bool = False  # Показывает, является ли текущая строка комментарием

                    for line in py_file:
                        # блок комментариев, комментарии и пустые строки - не берем в расчет
                        if re.match(r"\s*\"\"\".*|.*\'\'\'.*", line) and not comment:
                            comment = True
                        elif re.match(r".*\"\"\".*|.*\'\'\'\s*", line) and comment:
                            comment = False
                        elif re.match(r"^\s*$|^\s*#.*$", line) or comment:
                            continue
                        else:
                            count_lines += 1

                    # print(f'{os.path.join(root, file)} : {count_lines}')  # для проверки работы метода
                    yield count_lines


# print()
# for num_lines in gen_num_strings(os.path.abspath('..')):
#     print(num_lines, end=' ')
