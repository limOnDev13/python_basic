from typing import Optional
import re
from datetime import date


class Date:
    """
    Класс - дата. Проверяет корректность даты и конвертирует строку в объект Date

    Args:
        day (int) - день
        month (int) - месяц
        year (int) - год

    Raise:
        SyntaxError - объект инициализирован не через метод .from_string
    """
    __init_from_class: bool = False  # Показывает, была ли инициализация через метод from_string

    def __init__(self, day: int, month: int, year: int):
        if not self.__init_from_class:
            raise SyntaxError('Инициализация только через метод .from_string()!')
        self.__day: Optional[int] = day
        self.__month: Optional[int] = month
        self.__year: Optional[int] = year

    def __str__(self) -> str:
        return f'{self.__day}.{self.__month}.{self.__year}'

    # По условию установление даты только через преобразование строки, поэтому у класса будут только геттеры
    @property
    def day(self) -> Optional[int]:
        return self.__day

    @property
    def month(self) -> Optional[int]:
        return self.__month

    @property
    def year(self) -> Optional[int]:
        return self.__year

    @classmethod
    def __get_num_from_str(cls, string: str, start_index: int) -> tuple[int, int]:
        """
        Метод берет строку, начиная с start_index ищет подстроку в string, которая является числом. Пример:
        string = 'abc123def', start_index = 3, метод вернет 123
        :param string: Строка с числами
        :type string: str
        :param start_index: Начальный индекс, откуда ведется поиск
        :type start_index: int
        :raise: Если string[start_index] не является числом, то выбросится TypeError. Если start_index >= длина string,
        то выброситься IndexError
        :return: Два значения, первое - число из строки string, второе - индекс символа, на котором закончился поиск
        :rtype: tuple[int, int]
        """
        if not string[start_index].isdigit():
            raise TypeError(f'Символ по индексу {start_index} в строке {string} не является числом!')

        end_index: int = start_index

        while end_index < len(string) and string[end_index].isdigit():
            end_index += 1

        return int(string[start_index: end_index]), end_index

    @classmethod
    def from_string(cls, date_string: str) -> 'Date':
        """
        Метод для преобразования строкового представления даты
        :param date_string: Дата в строковом представлении
        :type date_string: str
        :raise: KeyError, если строка имеет формат, отличный от дд-мм-гггг;
                Exception, если введенная дата не существует
        :return: self
        :rtype: Date
        """
        # 1) Проверим, что строка соответствует формату
        if not re.match(r'\d{1,2}\D\d{1,2}\D\d{1,4}', date_string):
            raise KeyError('Введенная строка имеет неверный формат (дд-мм-гггг)!')

        # 2) Проверим валидность введенной даты
        day: int = 0
        month: int = 0
        year: int = 0
        start_index: int = 0

        day, start_index = cls.__get_num_from_str(string=date_string, start_index=start_index)
        month, start_index = cls.__get_num_from_str(string=date_string, start_index=start_index + 1)
        year, _ = cls.__get_num_from_str(string=date_string, start_index=start_index + 1)

        try:
            date(day=day, month=month, year=year)
        except ValueError:
            raise ValueError('Введенная дата невалидная!')
        else:
            cls.__init_from_class = True
            object_date: Date = Date(day, month, year)
            cls.__init_from_class = False
            return object_date


print('Попробуем обычную дату 10-12-2077')
date1: Date = Date.from_string('10-12-2077')
print(date1)

print('\nПопробуем несуществующую дату 32-12-2077')
try:
    date2: Date = Date.from_string('32-12-2077')
    print(date2)
except ValueError:
    print('Не получилось с датой 32-12-2077')

print('\nПопробуем неправильный формат со строкой ыворавыор')
try:
    date3: Date = Date.from_string('ыворавыор')
    print(date3)
except KeyError:
    print('Не получилось со строкой ыворавыор')

print('\nПопробуем инициализировать через __init__')
try:
    date4: Date = Date(day=1, month=2, year=1999)
    print(date4)
except SyntaxError:
    print('Не получилось инициализировать через __init__')

# Прост
date5: Date = Date.from_string('10@12:2077')
print()
print(date5)
