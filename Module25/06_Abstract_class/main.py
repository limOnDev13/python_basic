from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Базовый класс - фигура"""
    @abstractmethod
    def area(self) -> float:
        """
        Метод для расчета площади фигуры
        :return: Площадь фигуры
        :rtype: float
        """
        pass


class Circle(Shape):
    """
    Класс - окружность, родитель: Shape

    Args:
        radius (float) - радиус окружности
    """
    def __init__(self, radius: float):
        self.__radius: float = radius

    def area(self) -> float:
        """
        Метод возвращает площадь окружности
        :return: Площадь окружности
        :rtype: float
        """
        return pi * self.__radius ** 2


class Rectangle(Shape):
    """
    Класс - прямоугольник, родитель: Shape

    Args:
        a (float) - одна сторона прямоугольника
        b (float) - вторая сторона прямоугольника
    """

    def __init__(self, a: float, b: float):
        self.__a: float = a
        self.__b: float = b

    def area(self) -> float:
        """
        Метод возвращает площадь прямоугольника
        :return: Площадь окружности
        :rtype: float
        """
        return self.__a * self.__b


class Triangle(Shape):
    """
    Класс - прямоугольник, родитель: Shape

    Args:
        side (float) - одна сторона треугольника
        height (float) - высота к этой стороне
    """

    def __init__(self, side: float, height: float):
        self.__side: float = side
        self.__height: float = height

    def area(self) -> float:
        """
        Метод возвращает площадь прямоугольника
        :return: Площадь окружности
        :rtype: float
        """
        return self.__side * self.__height / 2


# Примеры работы с классом:
# Создание экземпляров классов
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Вычисление площади фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

# Вывод результатов
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)

# shape: Shape = Shape()
