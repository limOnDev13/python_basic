list_names: list[str] = ['Артемий', 'Борис',
                         'Влад', 'Гоша', 'Дима',
                         'Евгений', 'Женя', 'Захар']
new_list_names: list[str] = list()

for index, name in enumerate(list_names):
    if index % 2 == 0:
        new_list_names.append(name)

print('Первый день:', new_list_names)
