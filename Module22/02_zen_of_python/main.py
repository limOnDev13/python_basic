def read_and_write_reversed(in_file: str, out_file: str):
    """
    Функция считывает строки в in_file и записывает строки в обратном
    порядке в out_file. Файл out_file будет перезаписываться.
    :param in_file: Название (путь) файла с входными данными.
    :param out_file: Название (путь) файла куда будут записываться результат.
    :return: Ничего
    """
    with open(in_file, 'r', encoding='utf-8') as input_file:
        with open(out_file, 'w') as output_file:
            for line in reversed(list(input_file)):
                output_file.write(line)


read_and_write_reversed('zen.txt', 'reversed_zen.txt')
