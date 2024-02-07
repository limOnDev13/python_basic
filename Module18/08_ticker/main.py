def shifted_string(init_string: str, shift: int) -> str:
    """
    Функция производит сдвиг строки.
    :param init_string: Начальная строка.
    :param shift: Длина сдвига.
    :return: Сдвинутую строку.
    """
    syms: list[str] = [
        init_string[(index - shift) % len(init_string)]
        for index in range(len(init_string))
    ]
    return ''.join(syms)


first_string: str = input('Первая строка: ')
second_string: str = input('Вторая строка: ')

# Если длины строк не совпадают, то можно не начинать проверку
if len(first_string) != len(second_string):
    print('Первую строку нельзя получить из второй'
          ' с помощью циклического сдвига.')
    exit()

# Проверим все сдвиги от 0 до len - 1
for shift in range(len(first_string) - 1):
    if first_string == shifted_string(second_string, shift):
        print('Первая строка получается из второй со сдвигом {}.'.format(shift))
        break
else:
    print('Первую строку нельзя получить из второй'
          ' с помощью циклического сдвига.')
