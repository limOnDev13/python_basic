from random import uniform


def lucky_number(output_file: str = 'out_file.txt'):
    """
    Функция выполняет основной функционал задачи.
    :param output_file: Имя файла, куда будет сохраняться результат.
    :return: Ничего.
    """
    total_sum: int = 0
    nums: list[int] = list()

    while total_sum < 777:
        try:
            new_num: int = int(input('Введите число: '))
            total_sum += new_num

            # Условие неудачи
            if uniform(0, 1) < 1 / 13:
                raise ValueError('Неудача!')

            nums.append(new_num)
        except ValueError:
            print('Вас постигла неудача!')
            break
    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')

    # Сохраним результат
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join([str(num) for num in nums]))


lucky_number()
