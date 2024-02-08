def arrays_intersection(arr1: list[int],
                        arr2: list[int],
                        arr3: list[int]) -> list[int]:
    return [
        num
        for num in arr1
        if num in arr2 and num in arr3
    ]


def sets_intersection(arr1: list[int],
                      arr2: list[int],
                      arr3: list[int]) -> set[int]:
    set1: set[int] = set(arr1)
    set2: set[int] = set(arr2)
    set3: set[int] = set(arr3)
    return set1 & set2 & set3


def arrays_difference(arr1: list[int],
                      arr2: list[int],
                      arr3: list[int]) -> list[int]:
    return [
        num
        for num in arr1
        if num not in arr2 and num not in arr3
    ]


def sets_difference(arr1: list[int],
                    arr2: list[int],
                    arr3: list[int]) -> set[int]:
    set1: set[int] = set(arr1)
    set2: set[int] = set(arr2)
    set3: set[int] = set(arr3)
    return set1 - set2 - set3


def correct_print(arr: list[int] | set[int]):
    """
    Функция для корректной печати.
    :param arr: Список или множество.
    :return: Ничего.
    """
    for elem in arr:
        print(elem, end=' ')


array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# 1. Найти элементы, которые есть в каждом списке
print('Задача 1:')
print('Решение без множеств: ', end='')
correct_print(arrays_intersection(array_1, array_2, array_3))
print('\nРешение с множествами: ', end='')
correct_print(sets_intersection(array_1, array_2, array_3))

# 2. Найти элементы из первого списка, которых нет во втором и третьем списках.
print('\nЗадача 2:')
print('Решение без множеств: ', end='')
correct_print(arrays_difference(array_1, array_2, array_3))
print('\nРешение с множествами: ', end='')
correct_print(sets_difference(array_1, array_2, array_3))
