from typing import Any
from collections import OrderedDict


class Node:
    """
    Класс - узел

    Args:
        item (Any) - значение на узле
        prev_node (Node | None) - Ссылка на предыдущий узел. Если узел первый, то None.
    """
    def __init__(self, item: Any, prev_node=None):
        self.__item: Any = item
        self.__prev_node: Node | None = prev_node

    def get_item(self) -> Any:
        """
        Геттер для получения значения на узле
        :return: __item
        """
        return self.__item

    def get_prev_node(self):
        """
        Геттер для получения ссылки на предыдущий узел
        :return: __prev_node
        :rtype: Node | None
        """
        return self.__prev_node

    def set_prev_node(self, node):
        """
        Сеттер для установления ссылки на предыдущий узел. Нужен для метода удаления из стека.
        :param node: Новый узел
        :type node: Node | None
        :raise TypeError: выбрасывается, если передать что-то, что не является Node или None
        :return:
        """
        if not isinstance(node, None | Node):
            raise TypeError('Узел может содержать ссылку только на объект Node или None!')
        self.__prev_node = node


class SimpleStack:
    """
    Класс для простой реализации стека.
    """
    def __init__(self):
        self.__count: int = 0
        self.__last_node: Node | None = None

    def put(self, item: Any):
        """
        Метод для добавления элемента на верх стека
        :param item: Значение, сохраняемое в стеке
        :return:
        """
        self.__last_node = Node(item, self.__last_node)
        self.__count += 1

    def get(self) -> Any:
        """
        Метод для получения и удаления последнего элемента в стеке
        :raise IndexError: Выбрасывается, если попробовать извлечь элемент из пустого стека
        :return: Последний элемент в стеке
        """
        if self.__last_node is None:
            raise IndexError('Стек пуст!')

        last_item: Any = self.__last_node.get_item()
        self.__last_node = self.__last_node.get_prev_node()
        self.__count -= 1
        return last_item

    def delete(self, item: Any):
        """
        Метод для удаления значения из стека. Удаляется первый элемент с совпадающим значением
        :param item: Элемент, который необходимо удалить
        :raise ValueError: Выбрасывается, если в стеке нет такого элемента
        :return:
        """
        # Создадим список
        temp_stack: list = list()

        # Будем вынимать элементы из стека, пока не найдем необходимый
        try:
            while True:
                stack_item: Any = self.get()
                if type(stack_item) is type(item) and stack_item == item:
                    break
                else:
                    temp_stack.append(stack_item)
            # Если мы нашли нужный элемент и не было ошибки, то добавим все элементы,
            # начиная с последнего, обратно в стек
            while temp_stack:
                self.put(temp_stack.pop())
        except IndexError:
            print(f'{item} нет в стеке!')

    def get_all(self) -> list[Any]:
        """
        Метод для получения всех элементов стека
        :return: Список значений в стеке
        """
        result_list: list[int] = list()
        current_node: Node | None = self.__last_node

        for _ in range(self.__count):
            result_list.append(current_node.get_item())
            if current_node.get_prev_node() is not None:
                current_node = current_node.get_prev_node()

        return result_list


class TaskManager:
    """
    Класс - менеджер задач
    """
    def __init__(self):
        self.__tasks_stack: SimpleStack = SimpleStack()
        self.__set_tasks: set = set()

    def new_task(self, task: str, priority: int):
        """
        Метод для добавления новой задачи в менеджере.
        :param task: Текст задачи
        :type task: str
        :param priority: Приоритет задачи
        :type priority: int
        :return:
        """
        if task not in self.__set_tasks:
            self.__tasks_stack.put((task, priority))
            self.__set_tasks.add(task)
        else:
            raise KeyError('Такая задача уже есть в менеджере!')

    def delete_task(self, task: str):
        """
        Метод для удаления задачи из менеджера
        :param task: Текст задачи
        :type task: str
        :raise ValueError: Выбрасывает, если попытаться удалить несуществующую задачу.
        :return:
        """
        full_tasks: list[tuple[str, int]] = self.__tasks_stack.get_all()
        for task_text, priority in full_tasks:
            if task == task_text:
                self.__tasks_stack.delete((task, priority))
                break
        else:
            raise ValueError(f'Задачи {task} нет в стеке!')

    def __str__(self):
        # Чтобы получить строковое представление класса, сначала соберем словарь
        # с ключами из приоритетов и значениями - списками задач
        list_tasks: list[tuple[str, int]] = self.__tasks_stack.get_all()
        task_dict: dict[int, list[str]] = dict()

        for task in list_tasks:
            if task[1] in task_dict:
                task_dict[task[1]].append(task[0])
            else:
                task_dict[task[1]] = [task[0]]

        # Теперь соберем итоговую строку
        result_string: str = '\n'.join(
            [
                ' '.join([str(priority), '; '.join(tasks)])
                for priority, tasks in sorted(task_dict.items(), key=lambda x: x[0])
             ]
        )
        return result_string


manager: TaskManager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)

# Проверка удаления задачи и дубликатов
# print()
# manager.delete_task('помыть посуду')
# print(manager)
# print()
#
# manager.new_task("сделать уборку", 4)
# print(manager)
