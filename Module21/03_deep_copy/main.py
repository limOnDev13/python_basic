from copy import deepcopy


site: dict = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def create_site(name_product: str, **kwargs) -> dict:
    """
    Функция копирует макет сайта, заменяет название продукта,
    если переданны именнованные параметры - заменяет или добавляет новые параметры.
    Название параметра - путь по структуре, разделенные "."
    (например, "html.body.h3"),
    значение - новое значение для данного ключа.
    :param name_product: Название продукта.
    :return: Словарь - структуру нового сайта.
    """
    new_site: dict = deepcopy(site)
    # Заменим название продукта
    new_site['html']['head']['title'] = 'Куплю/продам ' + name_product + ' недорого'
    new_site['html']['body']['h2'] = 'У нас самая низка цена на ' + name_product

    return new_site


def correct_print_struct(struct: dict, number_indents: int = 0):
    """
    Функция для красивой и корректной печати структуры.
    Структура обходится с помощью рекурсии.
    :param struct: Структура
    :param number_indents: Количество отступов (табуляций).
    :return: Ничего
    """
    for key, value in struct.items():
        if isinstance(value, dict):
            print('\t' * number_indents + "'{}': ".format(key) + '{')
            correct_print_struct(value, number_indents + 1)
            print('\t' * number_indents + '}')
        else:
            print('\t' * number_indents + "'{}': {}".format(key, value))


def correct_print(structs: list[dict], names: list[str]):
    """
    Функция для красивой и корректной печати списка структур.
    Обходим структуру с помощью рекурсии.
    :param structs: Список структур.
    :param names: Названия продуктов.
    :return: Ничего.
    """
    for name, struct in zip(names, structs):
        print('Сайт для {}:'.format(name))
        print('site = {')
        correct_print_struct(struct, number_indents=1)
        print('}\n')


number_sites: int = int(input('Сколько сайтов: '))
sites: list[dict] = list()
names_sites: list[str] = list()

for _ in range(number_sites):
    new_product: str = input('Введите название продукта для нового сайта: ')
    sites.append(create_site(new_product))
    names_sites.append(new_product)
    correct_print(structs=sites, names=names_sites)

