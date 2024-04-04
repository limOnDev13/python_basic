from collections import Counter


def can_be_poly(string: str) -> bool:
    """
    Функция, которая проверяет, можно ли сделать из string палиндром
    :param string: Строка
    :type string: str
    :return: True, если из string можно сделать палиндром
    :rtype: bool
    """
    hist: Counter = Counter()

    for sym in string:
        hist[sym] += 1

    odd_characters: list[tuple[str, int]] = list(filter(lambda symbol: hist[symbol] % 2 == 1, hist))
    if len(odd_characters) > 1:
        return False
    return True


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
