from random import randint


number: int = 10
limits: tuple[int, int] = (1, 100)
init_list: list[int] = [randint(limits[0], limits[1])
                        for _ in range(number)]
print('Оригинальный список:', init_list)

# Срез списка в кортеж
new_list1: list[tuple[int, ...]] = [
    tuple(init_list[i: i + 2])
    for i in range(0, number, 2)
]
print('1 Способ:', new_list1)

# Через zip
new_list2: list[tuple[int, int]] = [
    (first_elem, second_elem)
    for first_elem, second_elem in zip(init_list[::2], init_list[1::2])
]
print('2 Способ:', new_list2)

# Через обращение по индексу к элементам списка (в тупую - кончилась фантазия)
new_list3: list[tuple[int, int]] = [
    (init_list[i], init_list[i + 1])
    for i in range(0, len(init_list) - 1, 2)
]
print('3 Способ:', new_list3)
