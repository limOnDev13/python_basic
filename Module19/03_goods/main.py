goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


def get_purchase_information(info: list[dict[str, int]]
                             ) -> tuple[int, int]:
    """
    Вспомогательная функция для получения общей информации о закупке.
    Метод получает список словарей (как в store) и считает
    общие количество и стоимость закупки.
    :param info: Список словарей с информацией о закупке. Словари имеют вид:
    {'quantity': ..., 'price': ...}
    :return: Количество и общая стоимость купленных товаров.
    """
    quantity: int = sum([info_dict['quantity']
                         for info_dict in info])
    total_price: int = sum([
        info_dict['quantity'] * info_dict['price']
        for info_dict in info
    ])

    return quantity, total_price


for good in goods:
    good_number, good_price = get_purchase_information(
        info=store[goods[good]]
    )
    print('{name} - {number} штук, стоимость - {price} рубля'.format(
        name=good,
        number=good_number,
        price=good_price
    ))
