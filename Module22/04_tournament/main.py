import random
from string import ascii_uppercase, ascii_lowercase


def generate_name() -> str:
    """
    Функция генерирует случайное имя.
    :return: Сгенерированное имя.
    """
    # Первая буква - заглавная
    letters_in_name: list[str] = [random.choice(ascii_uppercase)]
    # Остальные буквы - строчные
    letters_in_name.extend([random.choice(ascii_lowercase)
                            for _ in range(random.randint(0, 10))])

    return ''.join(letters_in_name)


def create_random_input(in_file: str = 'first_tour.txt'):
    """
    Так как в папке нет файла first_tour.txt, сгенерируем его случайно.
    Файл будет перезаписываться.
    :param in_file: Название файла, куда будут записываться входные данные.
    :return: Ничего.
    """
    num_k: int = random.randint(0, 100)
    num_members: int = random.randint(1, 10)

    with open(in_file, 'w') as file:
        # Запишем информацию согласно заданию.
        file.write(str(num_k) + '\n')
        for _ in range(num_members):
            member_info: str = ' '.join([generate_name(),
                                         generate_name(),
                                         str(random.randint(0, 100))])

            file.write('{}\n'.format(member_info))


def save_info_about_second_tour(in_file: str = 'first_tour.txt',
                                out_file: str = 'second_tour.txt'):
    """
    Функция сохраняет в файл out_file информацию о втором туре.
    Файл будет перезаписываться.
    :param in_file: Название (путь) файла с информацией о первом туре.
    Порядок информации об участнике: фамилия, имя, счет.
    :param out_file: Название (путь) файла, куда будет записываться результат.
    Порядок информации об участнике: номер участника, сокращенное имя, фамилия, счет.
    :return: Ничего.
    """
    with open(in_file, 'r', encoding='utf-8') as input_file:
        # Порог прохода во второй тур
        limit: int = int(input_file.readline())
        # Список прошедших во второй тур
        winners: list[str] = [member
                              for member in input_file
                              if int(member.split()[2]) > limit]
        winners.sort(key=lambda member: member.split()[2], reverse=True)

        # Запишем результат согласно заданию
        with open(out_file, 'w') as output_file:
            output_file.write('{}\n'.format(len(winners)))

            for num, member in enumerate(winners):
                output_file.write('{i_member}) {first_name}.'
                                  ' {second_name} {score}\n'.format
                                  (i_member=num + 1,
                                   first_name=member.split()[1][0],
                                   second_name=member.split()[0],
                                   score=member.split()[2]
                                   ))


create_random_input()
save_info_about_second_tour()
