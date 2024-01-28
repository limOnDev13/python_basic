number_people: int = int(input('Кол-во человек: '))
k: int = int(input('какое число в считалке? '))
print(f'Значит выбывает каждый {k}-й человек\n')
people: list[int] = list(range(1, number_people + 1))
start_index: int = 0

while len(people) > 1:
    print('Текущий круг людей:', people)
    print('Начало счета с номера', people[start_index])

    # Найдем позицию удаляемого человека
    removed_index: int = (start_index + k - 1) % len(people)
    print('Выбывает человек под номером', people[removed_index])
    people.remove(people[removed_index])

    # Изменим позицию, с кого начинается след круг
    start_index = removed_index
    # Если удалялся последний человек, то следующий будет на 0 позиции (т.к. они стоят в круг)
    if start_index == len(people):
        start_index = 0
    print()

print('Остался человек под номером', people[0])
