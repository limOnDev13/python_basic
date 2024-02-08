def it_is_palindrome(string: str) -> bool:
    """
    Функция проверяет, является ли строка палиндромом.
    :param string: Строка
    :return: True, если есть такая перестановка.
    """
    # Переведем строку в гистограмму частот в виде словаря
    histogram: dict[str, int] = dict()

    for sym in string:
        if sym in histogram:
            histogram[sym] += 1
        else:
            histogram[sym] = 1

    # Нечетная частота может быть только у одной буквы.
    # У всех остальных букв частота должна быть четной.
    # Только в этом случаем строку можно сделать палиндромом.
    num_odd_frequencies: int = 0
    for frequency in histogram.values():
        if frequency % 2 == 1:
            num_odd_frequencies += 1
        if num_odd_frequencies > 1:
            return False
    return True


text: str = input('Введите строку: ')

if it_is_palindrome(text):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
