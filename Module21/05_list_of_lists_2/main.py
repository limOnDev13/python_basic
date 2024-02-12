def expand_lists(lists: list) -> list[int]:
    """
    Функция рекурсивно раскрывает все вложенные списки.
    :param lists: Список элементов.
    :return: Раскрытый список.
    """
    result_list: list[int] = list()

    for elem in lists:
        if isinstance(elem, list):
            result_list.extend(expand_lists(elem))
        else:
            result_list.append(elem)

    return result_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(expand_lists(nice_list))
