print('Результат работы программы:')
main: list[int] = [1, 5, 3]
first_side_list: list[int] = [1, 5, 1, 5]
second_side_list: list[int] = [1, 3, 1, 5, 3, 3]

main.extend(first_side_list)
num5: int = main.count(5)
print('Кол-во цифр 5 при первом объединении:', num5)
for _ in range(num5):
    main.remove(5)

main.extend(second_side_list)
num3: int = main.count(3)
print('Кол-во цифр 3 при втором объединении:', num3)

print('Итоговый список:', main)
