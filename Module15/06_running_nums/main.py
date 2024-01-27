shift: int = int(input('Сдвиг: '))
init_list_nums_str: str = input('Изначальный список: ')

# Отредактируем ввод для удобной работы с ним
init_list_nums_str = init_list_nums_str[1: -1]
init_list_nums_split: list[str] = init_list_nums_str.split(', ')
init_list_nums: list[int] = [int(num) for num in init_list_nums_split]
result_list_nums: list[int]

# Если сдвиг больше длины списка,
# то возьмем его остаток по модулю длины списка
shift %= len(init_list_nums)

if shift == 0:
    # Если сдвиг нулевой, то просто выводим тот же список
    result_list_nums = init_list_nums
else:
    # Разобьем начальный список на два списка
    # 1 список - последние shift элементов
    first_part: list[int] = init_list_nums[-shift:]
    # 2 список - оставшиеся элементы
    second_part: list[int] = init_list_nums[0:len(init_list_nums) - shift]
    # Соединим полученные списки и получим необходимый сдвиг
    result_list_nums: list[int] = first_part + second_part

print('Сдвинутый список:', result_list_nums)
