def print_all_numbers(num_limit: int):
    """
    Функция с помощью рекурсии выводит все числа
    от 1 до num_limit включительно.
    :param num_limit: Верхняя граница чисел.
    :return: Ничего
    """
    if num_limit <= 1:
        print(1)
    else:
        print_all_numbers(num_limit - 1)
        print(num_limit)


num: int = int(input('Введите num: '))
print_all_numbers(num)
