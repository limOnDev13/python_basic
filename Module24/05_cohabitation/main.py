from random import randint


class Home:
    def __init__(self):
        self.food: int = 50
        self.piggy_bank: int = 0


class Human:
    eat_points: int = 10  # На сколько уменьшается еда и увеличивается сытость
    work_points: int = 12  # На сколько увеличиваются деньги на работе и уменьшается сытость
    store_points: int = 50  # Сколько тратится денег при походе в магазин и увеличивается еда
    play_points: int = 5  # Сколько тратится сытости при игре

    def __init__(self, name: str, home: Home, satiety_degree: int = 50):
        self.name: str = name
        self.satiety: int = satiety_degree
        self.home: Home = home

    def not_dead(self) -> bool:
        """
        Метод отвечает за смерть человека.
        :return: True, если бобик не помер, иначе - False.
        """
        if self.satiety <= 0:
            return False
        return True

    def eat(self):
        """
        Метод отвечает за потребление еды кожаным мешком.
        + сытость, - еда.
        :return: Ничего
        """
        # Если еды в холодильнике недостаточно - сходить в магазин.
        if self.home.food < self.eat_points:
            self.go_to_store()
        else:
            self.satiety += self.eat_points
            self.home.food -= self.eat_points

    def work(self):
        """
        Метод отвечает за поход человека на работу.
        - сытость, + деньги
        :return: Ничего.
        """
        self.satiety -= self.work_points
        self.home.piggy_bank += self.work_points

    def play(self):
        """
        Метод отвечает за игру человека.
        - сытость.
        :return: Ничего
        """
        self.satiety -= self.play_points

    def go_to_store(self):
        """
        Метод отвечает за поход в магазин.
        + еда, - деньги.
        :return: Ничего.
        """
        # Если денег недостаточно - идти на работу
        if self.home.piggy_bank < self.store_points:
            self.work()
        else:
            self.home.piggy_bank -= self.store_points
            self.home.food += self.store_points

    def live_one_day(self) -> bool:
        """
        Метод отвечает за жизнь за один день. Алгоритм будет взят из условия задачи.
        :return: True, если человек не умер, иначе - False.
        """
        # 1. Генерируется число кубика от 1 до 6
        roll: int = randint(1, 6)

        # 2. Если сытость < 20, то нужно поесть.
        if self.satiety < 20:
            self.eat()
        # 3. Иначе, если еды в доме < 10, то сходить в магазин.
        elif self.home.food < 10:
            self.go_to_store()
        # 4. Иначе, если денег в доме < 50, то работать.
        elif self.home.piggy_bank < 50:
            self.work()
        # 5. Иначе, если кубик равен 1, то работать.
        elif roll == 1:
            self.work()
        # 6. Иначе, если кубик равен 2, то поесть.
        elif roll == 2:
            self.eat()
        else:
            self.play()

        return self.not_dead()


home: Home = Home()
people: list[Human] = [Human(name=input('Введите имя: '), home=home)
                       for _ in range(2)]

for day in range(365):
    if not all([human.live_one_day() for human in people]):
        print(f'Ой, кто-то умер на {day} день!')
        break
else:
    print('Спустя 365 дней все живы.')
