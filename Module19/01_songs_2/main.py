violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}


def total_duration(songs: list[str]) -> float:
    """
    Метод возвращает общую длительность выбранных песен.
    :param songs: Список названий песен.
    :return: Суммарная длительность
    """
    # Избавимся от повторов названий
    set_songs: set[str] = set(songs)

    # Просуммируем все длительности с помощью get
    result_duration = sum([violator_songs.get(song, 0)
                           for song in set_songs])
    return result_duration


numbers_songs: int = int(input('Сколько песен выбрать? '))
songs_names: list[str] = [
    input('Название {} песни: '.format(num_ques))
    for num_ques in range(1, numbers_songs + 1)
]

print('\nОбщее время звучания песен: {} минуты'.format(
    total_duration(songs_names)
))
