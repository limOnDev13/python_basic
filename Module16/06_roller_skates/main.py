number_skates: int = int(input('Кол-во коньков: '))
sizes: list[int] = list()

for i in range(1, number_skates + 1):
    size: int = int(input(f'Размер {i}-й пары: '))
    sizes.append(size)

number_people: int = int(input('\nКол-во людей: '))
result_num: int = 0  # Количество людей, которые смогут взять коньки

for i in range(1, number_people + 1):
    size_leg: int = int(input(f'Размер ноги {i}-го человека: '))
    # Если введенный размер есть в списке, увеличим результат и удалим размер из списка
    if size_leg in sizes:
        result_num += 1
        sizes.remove(size_leg)

print('\nНаибольшее кол-во людей, которые могут взять ролики:', result_num)
