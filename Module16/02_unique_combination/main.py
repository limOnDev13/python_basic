def merge_sorted_lists(first_list: list[int], second_list: list[int]) -> list[int]:
    """
    Функция склеивает дваа отсортированных списка, убирает дубликаты и возвращает
    отсортированный результат. Вариант без использования множеств.
    :param first_list: Первый отсортированный список
    :param second_list: Второй отсортированный список
    :return: список, явлеяющийся отсортированной склейкой list1 и list2 без дубликатов
    """
    result_list: list[int] = list()

    # Соединим списки и отсортируем
    result_list.extend(first_list)
    result_list.extend(second_list)
    result_list.sort()

    # Пробежимся по каждому элементу, посчитаем количество одинаковых с ним
    # и удалим их на 1 раз меньше
    for num in result_list:
        amount_nums: int = result_list.count(num)
        for _ in range(amount_nums - 1):
            result_list.remove(num)

    return result_list


# def merge_sorted_lists(list1: list[int], list2: list[int]) -> list[int]:
#     # Простой вариант с использованием множеств
#     result_list: list[int] = list()
#
#     result_list.extend(list1)
#     result_list.extend(list2)
#
#     result_list = list(set(result_list))
#     return result_list


# Пример использования:
list1 = [1, 1, 1]
list2 = [1, 1, 1]
merged = merge_sorted_lists(list1, list2)
print(merged)
