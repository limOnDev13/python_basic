def correct_input(question: str) -> int:
    """
    Функция, отвечающая за корректный ввод.
    :param question: Текст вопроса
    :return: Число, удовлетворяющее условию
    """
    number: int = int(input(question))

    while number < 0 or number > 200:
        print('Ошибка! Все числа не могут быть отрицательным или больше 200!')
        number = int(input(question))

    return number


number_boxes: int = correct_input('Количество контейнеров: ')
boxes: list[int] = list()  # Хранит веса контейнеров

for _ in range(number_boxes):
    box: int = correct_input('Введите вес контейнера: ')
    boxes.append(box)

print()
new_box: int = correct_input('Введите вес нового контейнера: ')
print()

boxes.append(new_box)
number_boxes += 1  # Количество коробок увеличилось
boxes.sort(reverse=True)

matching_elem_i: int = boxes.index(new_box)  # Индекс первого совпадающего элемента
matching_elem_i += 1  # Индекс следующего за ним элемента
while matching_elem_i < number_boxes and boxes[matching_elem_i] == new_box:
    matching_elem_i += 1

print('Номер, который получит новый контейнер:', matching_elem_i)
