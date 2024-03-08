from typing import Literal


class Property:
    """
    Базовый класс, описывающий имущество налогоплательщиков

    Args:
        worth (float | None): стоимость имущества
    """
    def __init__(self, worth: float | None = None):
        self.__worth: float | None = worth  # Если None - то имущества нет
        self.__tax: float = 0.0

    def get_worth(self) -> float | None:
        """
        Геттер для получения стоимости имущества.
        :return: __worth
        :rtype: float | None
        """
        return self.__worth

    def get_tax(self) -> float:
        """
        Геттер для получения процента налога.
        :return: __tax
        :rtype: float
        """
        return self.__tax

    def set_tax(self, tax: float):
        """
        Сеттер для установления процента налога
        :param tax: Процент налога
        :type tax: float
        :return: Ничего
        """
        self.__tax = float(tax)

    def calculate_sum_tax(self) -> float:
        """
        Метод для расчета налога на имущество
        :return: Величину налога
        :rtype: float
        """
        if self.__worth is None:
            return 0.0
        return self.get_worth() * self.get_tax()

    def __str__(self) -> str:
        if self.__worth is None:
            return 'У вас нет {object}'.format(
                object=self.__class__.__name__
            )
        return "{object}:\n\tСтоимость: {worth}\n\tНалог: {tax}".format(
            object=self.__class__.__name__,
            worth=self.__worth,
            tax=self.calculate_sum_tax()
        )


class Apartment(Property):
    """
    Класс квартира. Родитель: Property

    Args:
        worth (float | None): стоимость имущества
    """
    def __init__(self, worth: float | None = None):
        super().__init__(worth)
        self.set_tax(1 / 1000)
        self.__class__.__name__ = 'Квартира'


class Car(Property):
    """
    Класс квартира. Родитель: Property

    Args:
        worth (float | None): стоимость имущества
    """

    def __init__(self, worth: float | None = None):
        super().__init__(worth)
        self.set_tax(1 / 200)
        self.__class__.__name__ = 'Машина'


class CountryHouse(Property):
    """
    Класс квартира. Родитель: Property

    Args:
        worth (float | None): стоимость имущества
    """

    def __init__(self, worth: float | None = None):
        super().__init__(worth)
        self.set_tax(1 / 500)
        self.__class__.__name__ = 'Дача'


def interface(obj_property: Literal['квартира', 'машина', 'дача']) -> Apartment | Car | CountryHouse:
    """
    Метод отвечает за взаимодействие с пользователем.
    :param obj_property: Тип имущества.
    :type obj_property: Literal['квартира', 'машина', 'дача']
    :return: Объект имущества, созданный на данных, введенных пользователем.
    :rtype: Apartment | Car | CountryHouse
    """
    object_worth: str = input('Имущество: {object}\n'
                              'Введите стоимость (если данного имущества нет, введите пустую строку): '.format(
                                object=obj_property
                              ))
    if obj_property == 'квартира':
        if object_worth:
            return Apartment(float(object_worth))
        else:
            return Apartment()
    if obj_property == 'машина':
        if object_worth:
            return Car(float(object_worth))
        else:
            return Car()
    if obj_property == 'дача':
        if object_worth:
            return CountryHouse(float(object_worth))
        else:
            return CountryHouse()


budget: float = float(input('Введите ваш бюджет: '))

apartment: Apartment = interface('квартира')
car: Car = interface('машина')
country_house: CountryHouse = interface('дача')

sum_tax: float = apartment.calculate_sum_tax() + car.calculate_sum_tax() + country_house.calculate_sum_tax()

for obj in apartment, car, country_house:
    print(obj)
if sum_tax > budget:
    print(f'Вам не хватает {sum_tax - budget}')
