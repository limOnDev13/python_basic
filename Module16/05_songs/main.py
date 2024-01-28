def find_song(list_songs: list[list[str | float]],
              required_name: str) -> float | None:
    """
    Функция ищет информацию о песне по названию и возвращает ее длительность.
    :param list_songs: Список информаций о песнях. Имеет вид списка списков,
     где 0-й элемент - название песни, 1-й - ее продолжительность.
    :param required_name: Название искомой песни.
    :return: продолжительность искомой песни или None, если такой песни нет.
    """
    for song in list_songs:
        if song[0] == required_name:
            return song[1]
    else:
        print('Такой песни нет в списке...')
        return None


violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

num_songs: int = int(input('Сколько песен выбрать? '))
total_time: float = 0.0

for i in range(1, num_songs + 1):
    song_name: str = input(f'Название {i}-й песни: ')
    song_info: float | None = find_song(violator_songs, song_name)

    if song_info is not None:
        total_time += song_info

print('Общее время звучания песен:', round(total_time, 2), 'минуты')
