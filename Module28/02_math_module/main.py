from math import pi


class Circle:
    """Класс для расчета параметров окружности"""
    @classmethod
    def circle_len(cls, radius: float) -> float:
        """
        Метод для расчета длины окружности
        :param radius: Радиус окружности
        :type radius: float
        :return: Длину окружности
        :rtype: float
        """
        return 2 * pi * radius

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        """
        Метод для расчета площади окружности
        :param radius: Радиус окружности
        :type radius: float
        :return: Площадь окружности
        """
        return pi * radius ** 2


class Cube:
    """Класс для расчета параметров куба"""
    @classmethod
    def cube_vol(cls, side: float) -> float:
        """
        Метод для расчета объема куба
        :param side: Длина ребра
        :type side: float
        :return: Объем куба
        :rtype: float
        """
        return side ** 3


class Sphere:
    """Класс для расчета параметров сферы"""
    @classmethod
    def sphere_sq(cls, radius: float) -> float:
        """
        Метод для расчета площади поверхности сферы
        :param radius: Радиус сферы
        :type radius: float
        :return: Площадь сферы
        :rtype: float
        """
        return 4 * pi * radius ** 2


class MyMath(Sphere, Cube, Circle):
    pass


# Проверка
res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)
