def move_letter(letter: str, move: int) -> str:
    """
    Функция получает букву и смещает ее по алфавиту (по круг) на сдвиг move.
    :param letter: Текст незашифрованного сообщения. В русском языке 33 буквы.
    :param move: Сдвиг.
    :return: Сдвинутая буква.
    """
    alfabet_upper: str = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alfabet_lower: str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    if letter in alfabet_upper:
        return alfabet_upper[(alfabet_upper.index(letter) + move) % 33]
    elif letter in alfabet_lower:
        return alfabet_lower[(alfabet_lower.index(letter) + move) % 33]
    else:
        return letter


text: str = input('Введите сообщение: ')
shift: int = int(input('Введите сдвиг: '))
code: list[str] = [
    move_letter(letter, shift)
    for letter in text
]

print('Зашифрованное сообщение:', ''.join(code))
