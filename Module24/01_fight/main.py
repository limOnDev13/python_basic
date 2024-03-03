from random import randint


class Warrior:
    damage: int = 20

    def __init__(self, index: int):
        self.health: int = 100  # Здоровье юнита
        self.index: int = index

    def damaged(self) -> bool:
        """
        Метод отвечает за получение урона. Если здоровье юнита
        закончилось, то юнит погибает.
        :return: True, если юнит погиб. Иначе - False
        """
        self.health -= Warrior.damage

        if self.health <= 0:
            return True
        return False

    def print_info(self):
        print('У война {} осталось {} здоровья.'.format(
            self.index, self.health))


class Fight:

    def __init__(self):
        self.unit1: Warrior = Warrior(1)
        self.unit2: Warrior = Warrior(2)

    def print_info(self):
        self.unit1.print_info()
        self.unit2.print_info()
        print()

    def fight(self) -> bool:
        """
        Метод отвечает за процесс битвы.
        :return: Если битва закончилась - True, иначе - False.
        """
        attacking_warrior: int = randint(1, 2)  # Атакующий выбирается случайно

        if attacking_warrior == 1:
            print('Воин {} нанес урон воину {}'.format(1, 2))
            if self.unit2.damaged():
                print('Воин {} одержал победу!'.format(1))
                return True

            self.print_info()
            return False
        else:
            print('Воин {} нанес урон воину {}'.format(2, 1))
            if self.unit1.damaged():
                print('Воин {} одержал победу!'.format(2))
                return True

            self.print_info()
            return False


fight_club: Fight = Fight()

while not fight_club.fight():
    pass
