# Реализация быстрой сортировки (опорный элемент - 0 элемент)
def qsort(list_nums: list[int]) -> list[int]:
    if len(list_nums) <= 1:
        return list_nums
    else:
        small_nums: list[int] = list()
        big_nums: list[int] = list()
        support_elem: int = list_nums[0]

        for index, num in enumerate(list_nums):
            if index > 0:
                if num < support_elem:
                    small_nums.append(num)
                else:
                    big_nums.append(num)

        return qsort(small_nums) + [support_elem] + qsort(big_nums)


# Обработка input (ввод в виде строки '[1, 2, 3]')
init_list_str: str = input('Изначальный список: ')
init_list_str = init_list_str[1:-1]
init_list_split: list[str] = init_list_str.split(', ')
init_list: list[int] = [int(num) for num in init_list_split]

print('Отсортированный список:', qsort(init_list))
