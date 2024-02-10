phonebook: dict[tuple[str, str], int] = dict()


def add_person():
    """
    Функция добавляет новый контакт в телефонную книгу.
    :return: Ничего.
    """
    first_name, second_name = input('Введите имя и фамилию'
                                    ' нового контакта: ').split()
    # Сделаем проверку наличия контакта в независимости от регистра.
    # Для этого создадим множество ключей в нижнем регистре и будем сравнивать по нему
    lower_keys: set[tuple[str, str]] = {
        (key[0].lower(), key[1].lower())
        for key in phonebook.keys()
    }
    if (first_name.lower(), second_name.lower()) in lower_keys:
        print('Такой человек уже есть в контактах.')
        return
    else:
        phonebook[(first_name, second_name)] = int(input('Введите номер телефона: '))


def search_man() -> list[str]:
    """
    Функция для поиска людей с указанной фамилией в телефонной книге.
    :return: Список строк с информацией о человеке
    """
    second_name = input('Введите фамилию для поиска: ')

    # Реализуем проверку без учета регистра. Для этого создадим множество
    # фамилий в нижнем регистре
    lower_second_names: set[str] = {
        key[1].lower()
        for key in phonebook.keys()
    }
    if second_name.lower() not in lower_second_names:
        print('Такого человека нет в телефонной книге.')
    else:
        return [
            ' '.join([name[0], name[1], str(phone)])
            for name, phone in phonebook.items()
            if second_name.lower() == name[1].lower()
        ]


def main():
    """
    Основная функция.
    :return: Ничего.
    """
    while True:
        # Ввод действия
        action: int = int(input('Введите номер действия:'
                                '\n1. Добавить контакт'
                                '\n2. Найти человека'
                                '\n3. Закончить\n'))
        if action == 1:
            add_person()
        elif action == 2:
            list_men: list[str] = search_man()
            for man_info in list_men:
                print(man_info)
        elif action == 3:
            print('Завершаю работу...')
            break

        print('Текущий словарь контактов:', phonebook)


main()
