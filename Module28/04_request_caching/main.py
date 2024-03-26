from queue import Queue
from typing import Any, Optional


class Node:
    """
    Класс - узел для хранения пар ключ - значение в очереди

    Args:
        key (Any) - ключ узла
        value (Any) - значение на узле
        next_node (Node) - ссылка на следующий узел
    """
    def __init__(self, key: Any, value: Any, next_node: Optional['Node']) -> None:
        self.__key: Any = key
        self.__value: Any = value
        self.__next_node: Optional[Node] = next_node

    @property
    def key(self) -> Any:
        return self.__key

    @property
    def value(self) -> Any:
        return self.__value

    @property
    def next_node(self) -> Optional['Node']:
        return self.__next_node

    @key.setter
    def key(self, key: Any) -> None:
        self.__key = key

    @value.setter
    def value(self, value: Any) -> None:
        self.__value = value

    @next_node.setter
    def next_node(self, next_node: Optional['Node']) -> None:
        self.__next_node = next_node


class MyQueue:
    """
    Класс - очередь

    Args:
        capacity (int) - Размер очереди
    """
    def __init__(self, capacity: int) -> None:
        self.__capacity: int = capacity
        self.__first_node: Optional[Node] = None
        self.__current_length: int = 0
        self.__current_node: Optional[Node] = None

    def __iter__(self) -> 'MyQueue':
        self.__current_node = self.__first_node
        return self

    def __next__(self) -> tuple[Any, Any]:
        if self.__current_node is None:
            raise StopIteration

        key: Any = self.__current_node.key
        value: Any = self.__current_node.value
        self.__current_node = self.__current_node.next_node
        return key, value

    def __get_last_node(self) -> tuple[Optional[Node], Optional[Node]]:
        """
        Метод возвращает ссылку на последний и предпоследний узлы
        :return: Последний узел в очереди
        :rtype: Optional[Node]
        """
        cur_node: Optional[Node] = self.__first_node
        previous_node: Optional[Node] = self.__first_node

        while cur_node is not None:
            previous_node = cur_node
            cur_node = cur_node.next_node

        return previous_node, cur_node

    def get(self, key: Optional[Any]) -> Any:
        """
        Метод возвращает значение по ключу. Значение переводится в начала очереди. Если ключ не указан (None),
        то возвращается последние значение в очереди
        :param key: Ключ
        :type key: Optional[Key]
        :return: Значение по ключу
        :rtype: Any
        """
        previous_node: Optional[Node] = None
        last_node: Optional[Node] = None

        if key is None:
            previous_node, last_node = self.__get_last_node()
            # Переместим последнее значение в начало очереди
            previous_node.next_node = None
            self.add(key=last_node.key, value=last_node.value)
        else:
            while


    def add(self, key: Any, value: Any) -> None:
        """
        Метод добавляет в очередь пару ключ - значение
        :param key: Ключ
        :type key: Any
        :param value: Значение
        :type value: Any
        :return: None
        """
        # Если очередь заполнена, то удаляем последний элемент
        if self.__current_length == self.__capacity:
            self.pop(need_delete=True)
        self.__first_node = Node(key, value, self.__first_node)
        self.__current_length += 1




class LRUCache:
    """
    Класс - кэш, для хранения недавно использованных запросов

    Args:
        capacity (int): Объем кэша
    """
    def __init__(self, capacity: int) -> None:
        self.__capacity: int = capacity
        self.__first_node: Optional[Node] = None

    @property
    def cache(self) -> Any:
        """
        Геттер для самого старого запроса
        :return: результат самого старого запроса
        :rtype: Any
        """
        first_value: Any = self.__c
        return self.__cache.get()







# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4