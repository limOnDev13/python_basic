def auxiliary_func(list_nums: list[int]) -> tuple[list[int], list[int], list[int]]:
    """
    Вспомогательная функция (сделана только по заданию). Разбивает список чисел на
    три списка: числа меньше последнего элемента, числа равные последнему элементу и
    числа больше последнего элемента.
    :param list_nums: Список чисел
    :return: Кортеж из трех списков чисел, согласно описанию функции.
    """
    support_element: int = list_nums[-1]
    small_nums: list[int] = [num for num in list_nums if num < support_element]
    equal_nums: list[int] = [num for num in list_nums if num == support_element]
    big_nums: list[int] = [num for num in list_nums if num > support_element]

    return small_nums, equal_nums, big_nums


def qsort(numbers: list[int]) -> list[int]:
    """
    Функция производит быструю сортировку чисел в списке.
    :param numbers: Список чисел.
    :return: Ничего.
    """
    # Условие остановки рекурсии
    if len(numbers) <= 1:
        return numbers

    lists_nums: tuple[list[int], list[int], list[int]] = auxiliary_func(numbers)

    result_list: list[int] = list()
    result_list.extend(qsort(lists_nums[0]))
    result_list.extend(lists_nums[1])
    result_list.extend(qsort(lists_nums[2]))

    return result_list


nums: list[int] = [4, 9, 2, 7, 5]
print(qsort(nums))
