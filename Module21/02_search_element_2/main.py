from typing import Any


def search_key(struct: dict[str, Any], key: str,
               depth: int | None = None) -> Any | None:
    """
    Функция ищет в переданной структуре данных значение по ключу
    при заданной глубине прохода структуры.
    Обход осуществляется с помощью рекурсии.
    :param struct: Структура данных в виде вложенных словарей.
    :param key: Искомый ключ.
    :param depth: Глубина прохода. Если depth is None,
    то глубина не задана, и поиск ведется по всей структуре.
    :return: Значение по заданному ключу. Если ключ не найден, то None.
    """
    # Если глубина поиска стала равна 0,
    # то возвращаем None - условие выхода из рекурсии.
    if depth is not None and depth <= 0:
        return None
    # Если глубина не задана или еще не равна 0,
    # то продолжаем поиск, пока не найдем.
    else:
        if key in struct:
            return struct[key]
        for struct_value in struct.values():
            if isinstance(struct_value, dict):
                result_value: Any | None

                if depth is None:
                    result_value = search_key(struct_value, key)
                else:
                    result_value = search_key(struct_value, key, depth - 1)

                # Если получили не None, то вернем result_value
                if result_value is not None:
                    return result_value
        # Если цикл полностью отработал, то мы не нашли нужный ключ, поэтому вернем None
        else:
            return None


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

required_key: str = input('Введите искомый ключ: ')
user_answer: str = input('Хотите ввести максимальную глубину? Y/N: ').lower()
searching_depth: int | None = None
if user_answer == 'y':
    searching_depth = int(input('Введите максимальную глубину: '))

print('Значение ключа:', search_key(site, required_key, searching_depth))
