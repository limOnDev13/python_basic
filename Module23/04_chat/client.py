"""
Модуль отвечает за работу клиента.
"""
import os
import time


class Client:
    users_file: str = 'users.txt'
    queue_file: str = 'queue.txt'

    def __init__(self, server_path: str, user_name: str):
        """
        Будем хранить id пользователя, его имя и директорию сервера.
        :param server_path: Путь до сервера.
        :param user_name: Имя пользователя.
        """
        # Чтобы присвоить id пользователю, нужно получить последний id в файле users.txt, который
        # хранится в директории с сервером.
        # Проверим, есть ли в данной директории скрипт server.py
        if not os.path.exists(os.path.join(server_path, 'server.py')):
            raise PermissionError('В данной директории не найден файл server.py')
        # Файл users.txt может быть открыт сервером, поэтому будем пробовать его открыть, пока не получится
        while True:
            try:
                with open(os.path.join(server_path, self.users_file), 'r', encoding='utf-8') as file_users:
                    # Информация users.txt записана в виде:
                    # <id клиента> <имя клиента> <директория клиента>\n
                    users_info: str = file_users.read()

                    if users_info:
                        users: list[str] = users_info.split('\n')
                        self.id: int = int(users[-2].split()[0]) + 1  # users[-1] == '\n'
                    # Если файл пустой, то self.id = 0
                    else:
                        self.id: int = 0

            except IOError:
                time.sleep(0.3)
            else:
                break

        self.name: str = user_name
        self.server_dir: str = server_path

        # Сохраним информацию о новом клиенте в users.txt
        while True:
            try:
                with open(os.path.join(server_path, self.users_file), 'a', encoding='utf-8') as file_users:
                    file_users.write('{id} {name} {path}\n'.format(
                        id=self.id,
                        name=self.name,
                        path=os.path.abspath('..')
                    ))
            except IOError:
                time.sleep(0.3)
            else:
                break


print()
client: Client = Client(
    server_path=os.path.abspath(''),
    user_name='Vova'
)
