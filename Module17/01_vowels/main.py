def get_list_vowel_letters(text: str) -> list[str]:
    """
    Функция генерирует список гласных букв из полученной строки.
    Учитывается только русский язык.
    :param text: Текст
    :return: Строка гласных букв.
    """
    vowel_letters: list[str] = ['у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю', 'ё']

    return [letter for letter in text if letter.lower() in vowel_letters]


msg: str = input('Введите текст: ')

list_vowel_letters: list[str] = get_list_vowel_letters(msg)

print('\nСписок гласных букв:', list_vowel_letters)
print('Длина списка:', len(list_vowel_letters))
