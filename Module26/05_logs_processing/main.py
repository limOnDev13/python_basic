import os
from typing import Iterable
import re


def error_log_generator(input_file: str) -> Iterable:
    """
    Генератор для получения строк, содержащие слово ERROR
    :param input_file: Имя (путь) к лог-файлу
    :type input_file: str
    :return: Строки со словом ERROR
    :rtype: Iterable
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as log_file:
            for line in log_file:
                if re.match(r'.*ERROR.*', line):
                    yield line
    except IOError as exc:
        print(exc)


# При помощи модуля os (и функции join) сформируйте пути до файлов work_logs.txt и output.txt в папке data
# (output.txt может не быть в папке data, но его нужно будет там создать, при помощи кода)
input_file_path = os.path.join(os.path.abspath(''), 'data', 'work_logs.txt')
output_file_path = os.path.abspath('error_logs.log')
# Документация по join https://docs-python.ru/standart-library/modul-os-path-python/funktsija-join-modulja-os-path/

# Не забудьте проверить наличие файлов перед тем как начать работу с ними
# https://docs-python.ru/standart-library/modul-os-path-python/funktsija-exists-modulja-os-path/

with open(output_file_path, 'w', encoding='utf-8') as output:
    for error_line in error_log_generator(input_file_path):
        output.write(error_line)
print("Файл успешно обработан.")
