films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

favorite_films: list[str] = list()
number_films: int = int(input('Сколько фильмов хотите добавить? '))

for _ in range(number_films):
    film_name: str = input('Введите название фильма: ')
    if film_name not in films:
        print('Ошибка: фильма', film_name, 'у нас нет :(')
        continue
    favorite_films.append(film_name)

print('Ваш список любимых фильмов: ', end='')
result_str: str = ''
for film in favorite_films:
    result_str += film + ', '
print(result_str[:-2])
