def get_frequencies_hist(string: str) -> dict[str, int]:
    """
    Функция из строки создает словарь частот букв.
    :param string: Строка.
    :return: Словарь, где ключи - символы в строке,
    значения - частоты букв в строке.
    """
    result_hist: dict[str, int] = dict()

    for sym in string:
        if sym in result_hist:
            result_hist[sym] += 1
        else:
            result_hist[sym] = 1

    return result_hist


def invert_dict(init_dict: dict[str, int]
                ) -> dict[int, list[str]]:
    """
    Инверитурет словарь, делая значения начального словаря
    ключами нового, а ключи старого - значениями нового.
    :param init_dict: Начальный словарь.
    :return: Инвертированный словарь. Ключи - частота,
    значения - списки символов с данной частотой.
    """
    new_keys: set[int] = set(init_dict.values())

    result_dict: dict[int, list[str]] = {
        key: [sym for sym in init_dict if init_dict[sym] == key]
        for key in new_keys
    }

    return result_dict


text: str = input('Введите текст: ')

print('Оригинальный словарь частот:')
hist: dict[str, int] = get_frequencies_hist(text)
for symbol in sorted(hist.keys()):
    print(symbol, ':', hist[symbol])

print('Инвертированный словарь частот:')
invert_hist: dict[int, list[str]] = invert_dict(hist)
for num in sorted(invert_hist.keys()):
    print(num, ':', invert_hist[num])
