import random
from monsters import MonsterHunter, Monster


class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и __str__ базового класса можно не вызывать (т.к. в них нету кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.
    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ", round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию, чтобы улучшить выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        # Каждый наследник должен выводить информацию о своём состоянии, чтобы вы могли отслеживать ход сражения
        raise NotImplementedError("Вы забыли переопределить метод __str__!")


class Healer(Hero):
    # Целитель:
    # Атрибуты:
    # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)
    # Методы:
    # - атака - может атаковать врага, но атакует только в половину силы self.__power
    # - получение урона - т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)
    # - исцеление - увеличивает здоровье цели на величину равную своей магической силе
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # исцеление) на выбранную им цель
    def __init__(self, name: str):
        super().__init__(name)
        # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)
        self.__magic_power: float = self.get_power() * 3
        self.__class__.__name__ = 'Хилер'

    def __str__(self) -> str:
        return 'Имя: {name}; класс: {class_obj}; здоровье: {hp}'.format(
            name=self.name,
            class_obj=self.__class__.__name__,
            hp=self.get_hp()
        )

    def attack(self, target: Monster):
        """
        Метод отвечает за атаку хиллера.
        :param target: Цель атаки.
        :type target: Monster
        :return: Ничего
        """
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage: float):
        """
        Метод отвечает за получение урона хиллером.
        :param damage: Урон
        :type damage: float
        :return: Ничего
        """
        self.set_hp(self.get_hp() - 1.2 * damage)
        super().take_damage(1.2 * damage)

    def heal(self, target: Hero):
        """
        Метод отвечает за исцеление союзника.
        :param target: Союзник.
        :type target: Hero
        :return: Ничего
        """
        target.set_hp(target.get_hp() + self.__magic_power)

    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # исцеление) на выбранную им цель
    def make_a_move(self, friends: list[Hero], enemies: list[Monster]):
        """
        Метод отвечает за ход хиллера.
        :param friends: Список союзников
        :type friends: list[Hero]
        :param enemies: Список врагов
        :type enemies: list[Monster]
        :return: Ничего
        """
        print(self.name, end=' ')
        target_of_heal = friends[0]
        min_health = target_of_heal.get_hp()
        for friend in friends:
            if friend.get_hp() < min_health:
                target_of_heal = friend
                min_health = target_of_heal.get_hp()

        if min_health < super().max_hp - 30 or not enemies:
            print("Исцеляет", target_of_heal.name)
            self.heal(target_of_heal)
        else:
            # Сначала будем выкашивать вражеских хиллеров, после остальных
            target_of_attack: Monster = enemies[0]
            enemies_have_healer: bool = False
            min_hp: float = 1e10  # Максимальное здоровье монстров - 150
            for enemy in enemies:
                if isinstance(enemy, MonsterHunter) and min_hp > enemy.get_hp():
                    target_of_attack = enemy
                    min_hp = enemy.get_hp()
                    enemies_have_healer = True

            # Если хиллеров не нашлось, то выбираем бойца с наименьшим здоровьем и вжариваем ему
            if not enemies_have_healer:
                for enemy in enemies:
                    if min_hp > enemy.get_hp():
                        target_of_attack = enemy
                        min_hp = enemy.get_hp()
                print('Атакует слабейшего -', target_of_attack.name)
            else:
                print("Атакует хиллера -", target_of_attack.name)

            self.attack(target_of_attack)
        print('\n')
        super().make_a_move(friends, enemies)




class Tank(Hero):
    # Танк:
    # Атрибуты:
    # - показатель защиты - изначально равен 1, может увеличиваться и уменьшаться
    # - поднят ли щит - танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
    # Методы:
    # - атака - атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)
    # - получение урона - весь входящий урон делится на показатель защиты (damage/self.defense) и только потом отнимается от здоровья
    # - поднять щит - если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но уменьшает показатель силы в 2 раза.
    # - опустить щит - если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает показатель силы в 2 раза.
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # поднять щит/опустить щит) на выбранную им цель
    def __init__(self, name: str):
        super().__init__(name)
        self.__defense: float = 1.0
        self.__raised_shield: bool = False
        self.__class__.__name__ = 'Танк'

    def __str__(self) -> str:
        return 'Имя: {name}; класс: {class_obj}; здоровье: {hp}'.format(
            name=self.name,
            class_obj=self.__class__.__name__,
            hp=self.get_hp()
        )

    def attack(self, target: Monster):
        """
        Метод отвечает за атаку танка.
        :param target: Цель атаки
        :type target: Monster
        :return: Ничего
        """
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage: float):
        """
        Метод отвечает за получение урона.
        :param damage: Урон
        :type damage: float
        :return: Ничего
        """
        self.set_hp(self.get_hp() - damage / self.__defense)
        super().take_damage(damage)

    def raise_shield(self):
        """
        Метод отвечает за поднятие щита
        :return: Ничего
        """
        if not self.__raised_shield:
            self.__defense *= 2
            self.set_power(self.get_power() / 2)
            self.__raised_shield = True

    def lower_shield(self):
        """
        Метод отвечает за опускание щита
        :return: Ничего
        """
        if self.__raised_shield:
            self.__defense /= 2
            self.set_power(self.get_power() * 2)
            self.__raised_shield = False

    def make_a_move(self, friends: list[Hero], enemies: list[Monster]):
        """
        Метод отвечает за один ход
        :param friends: Список союзников
        :type friends: list[Hero]
        :param enemies: Список врагов
        :type enemies: list[Monster]
        :return: Ничего
        """
        print(self.name, end=' ')
        # Цель любого танка - танчить
        if not self.__raised_shield:
            print('поднял щит')
            self.raise_shield()
        else:
            if not enemies:
                return
            # Всегда атакуем либо хиллера либо слабейшего всей толпой (Цитата Сплинтера)
            target_to_attack: Monster = enemies[0]
            min_hp: float = 1e10
            enemies_have_healer: bool = False

            for enemy in enemies:
                if isinstance(enemy, MonsterHunter) and min_hp > enemy.get_hp():
                    min_hp = enemy.get_hp()
                    target_to_attack = enemy
                    enemies_have_healer = True

            if enemies_have_healer:
                print("атакует хиллера -", target_to_attack.name)
            else:
                # Ищем слабейшего
                for enemy in enemies:
                    if min_hp > enemy.get_hp():
                        min_hp = enemy.get_hp()
                        target_to_attack = enemy
                print('атакует слабейшего -', target_to_attack.name)
            self.attack(target_to_attack)
        print('\n')
        super().make_a_move(friends, enemies)


class Attacker(Hero):
    # Убийца:
    # Атрибуты:
    # - коэффициент усиления урона (входящего и исходящего)
    # Методы:
    # - атака - наносит урон равный показателю силы (self.__power) умноженному на коэффициент усиления урона (self.power_multiply)
    # после нанесения урона - вызывается метод ослабления power_down.
    # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления урона - damage * (
    # self.power_multiply / 2)
    # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза
    # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # усиление, ослабление) на выбранную им цель
    def __init__(self, name: str):
        super().__init__(name)
        self.__power_multiply: float = 1.0
        self.__class__.__name__ = 'Дамагер'

    def __str__(self) -> str:
        return 'Имя: {name}; класс: {class_obj}; здоровье: {hp}'.format(
            name=self.name,
            class_obj=self.__class__.__name__,
            hp=self.get_hp()
        )

    def attack(self, target: Monster):
        """
        Метод отвечает за атаку
        :param target: Цель атаки
        :type target: Monster
        :return: Ничего
        """
        target.take_damage(self.get_power() * self.__power_multiply)
        self.power_down()

    def take_damage(self, damage: float):
        """
        Метод отвечает за получение урона
        :param damage: Величина урона
        :type damage: float
        :return: Ничего
        """
        self.set_hp(self.get_hp() - damage * self.__power_multiply / 2)
        super().take_damage(damage)

    def power_up(self):
        """
        Метод отвечает за усиление
        :return: Ничего
        """
        self.__power_multiply *= 2

    def power_down(self):
        """
        Метод отвечает за ослабление
        :return: Ничего
        """
        self.__power_multiply /= 2

    def make_a_move(self, friends: list[Hero], enemies: list[Monster]):
        """
        Метод отвечает за один ход
        :param friends: Список союзников
        :type friends: list[Hero]
        :param enemies: Список врагов
        :type enemies: list[Monster]
        :return:
        """
        print(self.name, end=' ')
        if self.__power_multiply < 4 or not enemies:
            print('использует усиление')
            self.power_up()
        else:
            # Ищем и атакуем хилера
            min_hp: float = 1e7
            target_to_attack: Monster = enemies[0]
            enemies_have_healer: bool = False

            for enemy in enemies:
                if isinstance(enemy, MonsterHunter) and min_hp > enemy.get_hp():
                    min_hp = enemy.get_hp()
                    target_to_attack = enemy
                    enemies_have_healer = True

            if enemies_have_healer:
                print('Атакует хиллера -', target_to_attack.name)
            else:
                # Ищем и атакуем слабейшего
                for enemy in enemies:
                    if min_hp > enemy.get_hp():
                        min_hp = enemy.get_hp()
                        target_to_attack = enemy

                print('Атакует слабейшего -', target_to_attack.name)
            self.attack(target_to_attack)
        print('\n')
        super().make_a_move(friends, enemies)

