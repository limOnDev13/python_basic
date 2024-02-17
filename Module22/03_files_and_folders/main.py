import os


def get_dir_info(init_path: str) -> tuple[int, int, int]:
    """
    Функция выводит количество файлов, подкаталогов и размер директории.
    Обход происходит с помощью рекурсии.
    Функция не обрабатывает несуществующие директории (нет в задании и неохота запариваться)
    :param init_path: Путь до директории.
    :return: Количество файлов, количество подкаталогов, размер директории.
    """
    num_files: int = 0
    num_dirs: int = 0
    dir_size: int = 0

    for cur_obj in os.listdir(init_path):
        obj_path: str = os.path.join(init_path, cur_obj)

        if os.path.isdir(obj_path):
            num_dirs += 1
            res_tuple: tuple[int, int, int] = get_dir_info(obj_path)
            num_files += res_tuple[0]
            num_dirs += res_tuple[1]
            dir_size += res_tuple[2]
        else:
            num_files += 1
            dir_size += os.path.getsize(obj_path)

    return num_files, num_dirs, dir_size


init_dir: str = os.path.abspath(os.path.join('..', '..', 'Module14'))
result: tuple[int, int, int] = get_dir_info(init_dir)

print(init_dir)
print('Размер каталога (в Кб):', round(result[2] / 1024, 2))
print('Количество подкаталогов:', result[1])
print('Количество файлов:', result[0])

