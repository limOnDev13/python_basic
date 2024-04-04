import re


def print_cars_numbers(numbers: str) -> None:
    """
    Функция находит в переданной строке номера частных авто и такси и выводит на экран
    :param numbers: Строка с номерами автомобилей
    :type numbers: str
    :return: None
    """
    print('Список номеров частных автомобилей: ', end='')
    print(re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b', numbers))

    print('Список номеров такси: ', end='')
    print(re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{5,6}\b', numbers))


if __name__ == '__main__':
    example: str = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

    print_cars_numbers(example)
