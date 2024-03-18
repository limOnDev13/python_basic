from typing import Any, Optional, Iterator


class Node:
    """
    Класс - узел в односвязном списке. Хранит информацию о следующем узле
    Args:
        item (Any) - Значение узла
        next_node (Optional['Node']) - ссылка на следующий узел
    """
    def __init__(self, item: Any, next_node: Optional['Node']) -> None:
        self.__item: Any = item
        self.__next_node: Optional[Node] = next_node

    def get_item(self) -> Any:
        """
        Геттер для получения значения на узле
        :return: __item
        :rtype: Any
        """
        return self.__item

    def get_next_node(self) -> Optional['Node']:
        """
        Геттер для получения ссылки на следу.щий узел
        :return: __next_node
        :rtype: Optional['Node']
        """
        return self.__next_node

    def set_next_node(self, node: 'Node') -> None:
        """
        Сеттер для установления ссылки на следующий узел
        :param node: Ссылка на новый узел
        :type node: Node
        :return: None
        """
        self.__next_node = node

    def __del__(self):
        pass


class LinkedList:
    """
    Класс - односвязный список (направление - в сторону конца)
    Args:
        first_node (Optional[Node]) - ссылка на первый узел
    """
    def __init__(self, first_node: Optional[Node] = None) -> None:
        self.__first_node: Optional[Node] = first_node
        self.__cur_node: Optional[Node] = first_node

    def __str__(self) -> str:
        return ''.join(['[', ' '.join([str(elem.get_item()) for elem in iter(self)]), ']'])

    def append(self, item: Any) -> None:
        """
        Метод добавляет значение в начало списка.
        :param item: Значение
        :type item: Any
        :return: None
        """
        self.__first_node = Node(item=item,
                                 next_node=self.__first_node)

    def __iter__(self) -> Iterator:
        self.__cur_node = self.__first_node
        return self

    def __next__(self) -> Node:
        if self.__cur_node is None:
            raise StopIteration
        else:
            result_node: Node = self.__cur_node
            self.__cur_node = self.__cur_node.get_next_node()
            return result_node

    def get(self, index: int) -> Any:
        """
        Метод для получения элемента по индексу
        :param index: Индекс элемента
        :type index: int
        :return: Значение по индексу
        :rtype: Any
        """
        self_iter: Iterator = iter(self)

        try:
            for _ in range(index):
                next(self_iter)

            return self_iter.__next__().get_item()
        except StopIteration:
            raise IndexError

    def remove(self, index: int = 0) -> None:
        """
        Метод для удаления элемента по индексу
        :param index: Индекс элемента
        :type index: int
        :return: None
        """
        self_iter: Iterator = iter(self)

        try:
            for _ in range(index - 1):
                next(self_iter)

            first_node: Node = self_iter.__next__()
            removed_node: Node = self_iter.__next__()  # Переменная не нужно, написано для удобочитаемости
            second_node: Optional[Node] = None
            try:
                second_node = self_iter.__next__()
            except StopIteration:
                pass

            first_node.set_next_node(second_node)
        except StopIteration:
            raise IndexError


my_list = LinkedList()
# Элементы добавляются в НАЧАЛО списка - было проще и меньше писать
my_list.append(30)
my_list.append(20)
my_list.append(10)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
