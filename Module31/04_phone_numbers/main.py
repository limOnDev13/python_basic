import re


def check_phone_number(numbers: list[str]) -> None:
    """
    Функция проверяет список телефонных номеров согласно условию задачи
    :param numbers: Список телефонных номеров
    :type numbers: list[str]
    :return: None
    """
    for number in numbers:
        print(number, end=': ')
        if re.match(r'\b[89]\d{9}\b', number):
            print('все в порядке')
        else:
            print('не подходит')


if __name__ == '__main__':
    phone_numbers: list[str] = ['9999999999', '999999-999', '99999x9999']
    check_phone_number(phone_numbers)
