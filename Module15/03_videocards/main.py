number_video_cards: int = int(input('Количество видеокарт: '))
models: list[int] = list()

for i in range(number_video_cards):
    model: int = int(input(f'{i + 1} Видеокарта: '))
    models.append(model)

print('\nСтарый список видеокарт:', models)

oldest_model: int = max(models)
while oldest_model in models:
    models.pop(models.index(oldest_model))

print('Новый список видеокарт:', models)
