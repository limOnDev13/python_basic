from typing import Any, Optional


class Node:
    """
    Класс - узел для хранения пар ключ - значение в очереди

    Args:
        key (Any) - ключ узла
        value (Any) - значение на узле
        next_node (Node) - ссылка на следующий узел
    """
    def __init__(self, key: Any, value: Any, next_node: Optional['Node'] = None) -> None:
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
        self.__cur_node: Optional[Node] = None
        self.__prev_node: Optional[Node] = None

    def __iter__(self) -> 'MyQueue':
        self.__cur_node = self.__first_node
        self.__prev_node = self.__first_node
        return self

    def __next__(self) -> tuple[Optional[Node], Optional[Node]]:
        """
        Метод возвращает предыдущий и текущий узлы
        :return: предыдущий и текущий узлы соответственно
        :rtype: tuple[Optional[Node], Optional[Node]]
        """
        if self.__cur_node is None:
            raise StopIteration

        res_nodes: tuple[Optional[Node], Optional[Node]] = (self.__prev_node, self.__cur_node)
        self.__prev_node, self.__cur_node = self.__cur_node, self.__cur_node.next_node
        return res_nodes

    def __find_last_node(self) -> tuple[Optional[Node], Optional[Node]]:
        """
        Метод ищет и возвращает предпоследний и последний узлы в очереди. Код пару раз дублируется,
        поэтому вынесен в отдельный метод
        :return: предпоследний и последний узлы в очереди соответственно
        :rtype: tuple[Optional[Node], Optional[Node]]
        """
        prev_required_node: Optional[Node] = self.__first_node

        for index in range(1, self.__current_length - 1):
            prev_required_node = prev_required_node.next_node

        required_node: Optional[Node] = prev_required_node.next_node

        return prev_required_node, required_node

    def get(self, key: Optional[Any] = None) -> Any:
        """
        Метод возвращает значение по ключу из очереди. При этом значение переводится в начало очереди.
        Если ключ не указан (None), то возвращает значение из конца очереди.
        :param key: Ключ
        :type key: Optional[Any]
        :raise KeyError: Выбрасывает, если полученный ключ не найден
        :return: Значение по ключу
        :rtype: Any
        """
        required_node: Optional[Node] = None
        prev_required_node: Optional[Node] = None

        if key is None:
            # Если ключ не указан возвращаем значение из конца очереди
            prev_required_node, required_node = self.__find_last_node()
        else:
            # Ищем необходимый ключ
            for prev_node, node in self:
                if node.key == key:
                    required_node = node
                    prev_required_node = prev_node
                    break
            # Если цикл не был прерван, значит ключ не нашли
            else:
                raise KeyError(f'Ключ {key} не найден!')

        # Удаляем найденный узел и перемещаем его в начало очереди
        prev_required_node.next_node = required_node.next_node
        self.__first_node = required_node
        return required_node.value

    def pop(self) -> tuple[Any, Any]:
        """
        Метод удаляет последний узел в очереди и возвращает его ключ и значение
        :return: Ключ и значение на последнем узле
        :rtype: tuple[Any, Any]
        """
        required_node: Optional[Node] = None
        prev_required_node: Optional[Node] = None

        # Найдем последний узел
        prev_required_node, required_node = self.__find_last_node()

        # Удалим последний узел и вернем его ключ - значение
        prev_required_node.next_node = None
        self.__current_length -= 1
        return required_node.key, required_node.value

    def add(self, key: Any, value: Any) -> None:
        """
        Метод добавляет новые ключ - значение в начало очереди. Если очередь достигла предела длины,
        то последний элемент очереди удаляется
        :param key: Ключ
        :type key: Any
        :param value: Значение
        :type value: Any
        :return: None
        """
        if self.__current_length == self.__capacity:
            self.pop()

        self.__first_node = Node(key, value, self.__first_node)


class LRUCache:
    """
    Класс - кэш, для хранения недавно использованных запросов

    Args:
        capacity (int): Объем кэша
    """
    def __init__(self, capacity: int) -> None:
        self.__cache: MyQueue = MyQueue(capacity)

    def print_cache(self) -> None:
        """
        Печатает содержимое кэша. Можно было переписать __str__, но по примеру из задания нужно сделать этот метод
        :return: None
        """
        print('LRU Cache:')

        for _, node in self.__cache:
            print(f'{node.key}: {node.value}')

        print()

    def get(self, key: Optional[Any] = None) -> Any:
        """
        Метод возвращает значение по ключу (описание см в MyQueue.get)
        :param key: Ключ
        :type key: Optional[Any]
        :return: Значение по ключу
        :rtype: Any
        """
        return self.__cache.get(key)

    @property
    def cache(self) -> None:
        """Мне не нужен геттер, нужен только сеттер"""
        return None

    @cache.setter
    def cache(self, pair: tuple[Any, Any]) -> None:
        self.__cache.add(pair[0], pair[1])


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
print()

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4
