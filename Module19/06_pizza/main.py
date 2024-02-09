def print_dict_orders(dict_orders: dict[str, dict[str, int]]):
    """
    Функция отвечает за корректный вывод словаря.
    :param dict_orders: Словарь заказов.
    :return: Ничего.
    """
    for second_name in sorted(dict_orders.keys()):
        print('{}:'.format(second_name))
        for pizza in sorted(dict_orders[second_name]):
            print('\t{0}: {1}'.format(
                pizza, dict_orders[second_name][pizza]
            ))


# Хранить данные будем в виде словаря словарей.
# Во внешнем словаре ключом будет фамилия заказчика.
# Во вложенных словарях будем хранить информацию о заказанных пиццах.
num_orders: int = int(input('Введите количество заказов: '))

orders: dict[str, dict[str, int]] = dict()

# Не придумал как сделать через представление...
for i in range(num_orders):
    order: list[str] = input('{} заказ: '.format(i + 1)).split()
    if order[0] in orders:
        if order[1] in orders[order[0]]:
            orders[order[0]][order[1]] += int(order[2])
        else:
            orders[order[0]][order[1]] = int(order[2])
    else:
        orders[order[0]] = {order[1]: int(order[2])}

print()
print_dict_orders(orders)
