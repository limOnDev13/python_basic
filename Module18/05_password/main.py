def filter_for_password(password: str) -> bool:
    # Проверка на длину
    if len(password) < 8:
        return False

    # Проверка на наличие заглавной буквы и количество цифр
    count_nums: int = 0
    has_upper_letter: bool = False
    for letter in password:
        if letter.isupper():
            has_upper_letter = True
        if letter.isdigit():
            count_nums += 1

    if count_nums < 3 or not has_upper_letter:
        return False
    return True


text: str = input('Придумайте пароль: ')

while not filter_for_password(text):
    text = input('Пароль ненадёжный. Попробуйте ещё раз.\n'
                 'Придумайте пароль: ')

print('Это надежный пароль!')
