from dataclasses import dataclass
from random import randint, choices
from service import servise


class FamilyGuy:

    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age


@dataclass
class States:
    calm_state: bool = True
    hunger_state: bool = False


class Child(FamilyGuy):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.states: States = States()

    def calm_dawn(self):
        if self.states.calm_state:
            print('Ребенок и так спокоен...')
        else:
            self.states.calm_state = True

    def eat(self):
        if self.states.hunger_state:
            self.states.hunger_state = False
        else:
            print('Ребенок не голоден...')

    # def print_info(self, indents: int = 0):
    #     """
    #     Метод выводит информацию о ребенке.
    #     :param indents: Количество отступов для красоты вывода.
    #     :return: Ничего.
    #     """
    #     print('{indent}Имя ребенка: {name}\n{indent}Возраст: {age}\n'
    #           '{indent}Состояние спокойствия: {calm_state}\n'
    #           '{indent}Состояние голода: {hunger_state}\n'.format(
    #             indent='\t' * indents,
    #             name=self.name,
    #             age=self.age,
    #             calm_state=self.states.calm_state,
    #             hunger_state=self.states.hunger_state))


class Parent(FamilyGuy):

    def __init__(self, name: str, age: int, children: list[Child]):
        super().__init__(name, age)
        self.children: list[Child] = children
        if not all([self.age - child.age >= 16
                    for child in self.children]):
            raise ValueError('Возрасты детей должны быть меньше возраста родителя хотя бы на 16 лет!')

    def print_info(self):
        """
        Метод выводит информацию о родителе.
        :return: Ничего.
        """
        print('Имя родителя: {name}\nВозраст: {age}\nДети: {children}\n'.format(
            name=self.name,
            age=self.age,
            children=[child.name for child in self.children]
        ))

    def calm_dawn_child(self, child: Child):
        """
        Метод реализует функцию успокаивания ребенка. Необязательно своего...
        :param child: Объект ребенка.
        :return: Ничего.
        """
        print('Родитель {parent} успокаивает {child}'.format(
            parent=self.name,
            child=child.name
        ))
        child.calm_dawn()

    def feed_child(self, child: Child):
        """
        Метод реализует функцию кормления ребенка (необязательно своего).
        :param child: Объект ребенка.
        :return: Ничего.
        """
        print('Родитель {parent} кормит {child}'.format(
            parent=self.name,
            child=child.name
        ))
        child.eat()


# Код для тестирования работы классов
# children_list: list[Child] = [Child(
#     name=servise.generate_word(),
#     age=randint(0, 18)
# ) for _ in range(randint(1, 20))]
# parents_list: list[Parent] = [Parent(
#     name=servise.generate_word(),
#     age=randint(35, 100),
#     children=choices(children_list, k=randint(0, 3))  # У некоторых детей может быть больше 2 родителей -
#                                                       # не охота заморачиваться
# ) for _ in range(1, randint(1, 10))
# ]
#
# print(f'len(children_list) = {len(children_list)}')
# print(f'len(parents_list) = {len(parents_list)}\n')
# for parent in parents_list:
#     parent.print_info()
#     for child in parent.children:
#         child.print_info(1)
#
# print('\nИзменим статус ребенка и попробуем его изменить через родителя')
# # Изменим статус ребенка и попрбуем его изменить через родителя
# for parent in parents_list:
#     if not parent.children:
#         continue
#
#     print('Изменим состояние спокойствия:')
#     parent.children[0].states.calm_state = False
#     parent.children[0].print_info(1)
#     parent.calm_dawn_child(parent.children[0])
#     parent.children[0].print_info(1)
#     parent.calm_dawn_child(parent.children[0])
#     parent.children[0].print_info(1)
#
#     print('Изменим состояние голода:')
#     parent.children[0].states.hunger_state = True
#     parent.children[0].print_info(1)
#     parent.feed_child(parent.children[0])
#     parent.children[0].print_info(1)
#     parent.feed_child(parent.children[0])
#     parent.children[0].print_info(1)
#     break
