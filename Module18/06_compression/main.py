def encode_string(init_string: str) -> str:
    """
    Метод кодирует переданную строку указанным способом
    :param init_string: Начальная строка
    :return: Закодированная строка
    """
    letters: list[str] = list()  # Будет хранить буквы
    nums_letters: list[int] = list()  # Будет хранить количества повторяющихся букв.
    # Индекс буквы соответствует индексу количества.

    for letter in init_string:
        # Нужно добавить первую букву, чтобы не выйти за границу списка.
        if len(letters) == 0 or letter != letters[-1]:
            # Если буква изменилась, то добавляем новую в список letters,
            # а в список num_letters добавляем 1.
            letters.append(letter)
            nums_letters.append(1)
        else:
            nums_letters[-1] += 1

    # Собираем и возвращаем результат
    code_text: list[str] = [
        ''.join([letter, str(num)])
        for letter, num in zip(letters, nums_letters)
    ]
    return ''.join(code_text)


text: str = input('Введите строку: ')

print('Закодированная строка:', encode_string(text))
