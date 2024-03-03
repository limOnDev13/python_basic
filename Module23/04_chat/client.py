"""
Модуль отвечает за работу клиента.
"""
import os
import time
# from service import service_func


def create_file(file_name: str):
    """
    Функция создает файл.
    :param file_name: Имя файла.
    :return: Ничего.
    """
    try:
        with open(file_name, 'x', encoding='utf-8') as file:
            return
    except FileExistsError:
        return


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

        # Создадим файл <id клиента>_False.txt - в нем будет храниться полученная от сервера информация.
        create_file(f'{self.id}_False.txt')

        # Сохраним информацию о новом клиенте в users.txt
        while True:
            try:
                with open(os.path.join(server_path, self.users_file), 'a', encoding='utf-8') as file_users:
                    file_users.write('{id} {name} {path}\n'.format(
                        id=self.id,
                        name=self.name,
                        path=os.path.abspath('')
                    ))
            except IOError:
                time.sleep(0.3)
            else:
                break

    def set_command(self, *args):
        """
        Метод отправляет запрос серверу. Так как количество параметров для команды может быть различным,
        то используется *args.
        :param args: Параметры команды
        :return: Ничего.
        """
        # Соберем текст команды
        # Команда имеет вид: <id клиента> <id команды> <текст сообщения (необязательно)>\n
        command_params: list[str] = [str(self.id)]
        command_params.extend([str(i_item) for i_item in args])

        command: str = ' '.join(command_params)

        # Команду нужно добавить в очередь в файл queue.txt в директории сервера. Так как этот файл может быть открыт
        # сервером, то будем пробовать его открыть, пока не откроется
        while True:
            try:
                with open(os.path.join(self.server_dir, self.queue_file), 'a', encoding='utf-8') as queue:
                    queue.write(f'{command}\n')
            except IOError:
                time.sleep(0.1)
            else:
                break

    def get_data(self) -> str:
        """
        Метод возвращает полученную от сервера информацию. По условию задачи - это текст чата.
        :return: Полученную информацию.
        """
        # Сервер сохраняет информацию в директории клиента в файле <id клиента>_True.txt. Считаем ее и переименуем файл
        # в <id клиента>_False.txt
        # Будем проверять наличие файла <id клиента>_True.txt и пытаться его открыть, пока не откроем
        server_data: str = ''
        client_path_true: str = os.path.abspath(f'{self.id}_True.txt')
        client_path_false: str = os.path.abspath(f'{self.id}_False.txt')

        while True:
            try:
                with open(os.path.join(client_path_true), 'r', encoding='utf-8') as data:
                    server_data += data.read()

                # Переименуем файл
                os.rename(client_path_true, client_path_false)
            except IOError:
                time.sleep(0.1)
            else:
                break

        return server_data

    def loop(self):
        """
        Метод, отвечающий за основную работу клиента. Работает в бесконечном цикле.
        :return: Ничего.
        """
        while True:
            while True:
                try:
                    # Спросим у пользователя, какую команду выполнить
                    command_id: int = int(input('Введите команду: (1 - получить текст чата;'
                                                ' 2 - написать новое сообщение)\n'))
                    # Если введена несуществующая команда, выбросим исключение
                    if command_id not in [1, 2]:
                        raise ValueError(f'{command_id} - такой команды не существует!')
                except ValueError as exc:
                    print(exc)
                else:
                    break

            # Запросим выбранную команду у сервера и, если надо - получим от него данные (точнее напечатаем в консоли)
            msg_text: str = ''
            if command_id == 2:
                msg_text += input('Введите сообщение: ')
                self.set_command(command_id, msg_text)
            elif command_id == 1:
                self.set_command(command_id)
                print(self.get_data())


user_name: str = input('Здравствуйте! Введите ваше имя (одним словом): ')
server_dir: str = input('Введите директорию сервера:\n')
client: Client = Client(
    server_path=server_dir,
    user_name=user_name
)
client.loop()
