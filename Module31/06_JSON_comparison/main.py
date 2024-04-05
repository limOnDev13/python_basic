from typing import Optional
import json


def find_differences(old_dict: dict, new_dict: dict,
                     req_params: list[str], result_dict: dict,
                     current_path: Optional[str]) -> None:
    """
    Функция для рекурсивного обхода словарей и поиска отличий по параметрам из списка
    :param old_dict: Старый словарь
    :type old_dict: dict
    :param new_dict: Новый словарь
    :type new_dict: dict
    :param req_params: Список отслеживаемых параметров
    :type req_params: list[str]
    :param result_dict: Ссылка на выходной словарь. Лучше таскать его по всей рекурсии, и при нахождении
    различий тут же сохранять их в нем. Если различия находятся внутри вложенных словарей,
    то по тому же пути сохраняются различия и в выходной словарь.
    Т.е. если old_dict['a']['b'] = 1, new_dict['a']['b'] = 2, то result_dict['a']['b'] = 2
    :type result_dict: dict
    :param current_path: Путь до текущего параметра.
    Необходим для корректной работы рекурсии и сохранения результата в словарь
    :type current_path: Optional[str]
    :return: None (словарь с результатами тащится внутри входных параметров к этому методу)
    """


def compare(old_file: str, new_file: str, req_params: list[str]) -> dict:
    """
    Функция сравнивает два json файла по списку параметров. Изменившиеся параметры сохраняются в выходной словарь.
    Ключ - имя изменившегося параметра, значение - значение из файла new_file
    :param old_file: Имя старого json файла
    :type old_file: str
    :param new_file: Имя нового json файла
    :type new_file: str
    :param req_params: Список параметров, по которым идет сравнение. Если в файлах несколько одноименных параметров,
    будут отслеживаться все
    :type req_params: list[str]
    :raise KeyError: Если параметра из req_params нет в файлах
    :return: Словарь с изменившимся параметрами. Так как могут отслеживаться несколько одноименных параметров,
    то выходной словарь может иметь вложенные словари (вроде пути до измененного параметра)
    :rtype: dict
    """
    with open(old_file, 'r') as old_json:
        with open(new_file, 'r') as new_json:
            old_dict: dict = json.load(old_json)
            new_dict: dict = json.load(new_json)

            # Будем рекурсивно искать необходимые параметры
            for key, value in old_dict.values():
                pass
