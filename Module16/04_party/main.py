def add_new_quest(list_guests: list[str], name: str):
    """
    Функция отвечает за добовление нового гостя.
    :param list_guests: Список гостей.
    :param name: Имя нового гостя.
    :return: Ничего.
    """
    if len(list_guests) == 6:
        print(f'Прости, {name}, но мест нет.')
    else:
        list_guests.append(name)
        print(f'Привет, {name}!')


def remove_quest(list_quests: list[str], name: str):
    """
    Функция отвечает за удаление гостя из списка.
    :param list_quests: Список гостей.
    :param name: Имя гостя, который уходит.
    :return: Ничего.
    """
    if name in list_quests:
        print(f'Пока, {name}!')
        list_quests.remove(name)
    else:
        print('Такого гостя здесь нет...')


def correct_input() -> str:
    """
    Функция отвечает за корректный ввод
    :return: строку, отвечающую условиям.
    """
    user_answer: str = input('Гость пришел или ушел? ')

    while user_answer not in answers:
        print('Я не понимаю...')
        user_answer = input('Гость пришел или ушел? ')

    return user_answer


guests: list[str] = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
answers: list[str] = ['ушел', 'пришел', 'Пора спать']

print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
answer: str = correct_input()

while answer != 'Пора спать':
    guest_name: str = input('Имя гостя: ')

    if answer == 'пришел':
        add_new_quest(guests, guest_name)
    else:
        remove_quest(guests, guest_name)

    print(f'\nСейчас на вечеринке {len(guests)} человек: {guests}')
    answer = correct_input()

print('\nВечеринка закончилась, все легли спать.')

