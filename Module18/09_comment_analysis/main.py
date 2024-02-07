def count_uppercase_lowercase(string: str) -> tuple[int, int]:
    """
    Функция подсчитывает количество заглавных и строчных букв.
    :param string: Входная строка.
    :return: Количество заглавных и количество строчных букв.
    """
    num_upper: int = 0
    num_lower: int = 0

    for letter in string:
        if letter.isupper():
            num_upper += 1
        elif letter.islower():
            num_lower += 1

    return num_upper, num_lower


# Пример использования:
text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
