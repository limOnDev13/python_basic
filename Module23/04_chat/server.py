"""
Модуль отвечает за работу сервера. Является простейшим (и возможно кривым) аналогом.
"""
import time
# from service import service_func
import os


def create_file(file_name: str):
    """
    Функция создает файл. Пришлось скопировать сюда, т.к. Powershell не хочет импортировать его из service.
    :param file_name: Имя файла.
    :return: Ничего.
    """
    try:
        with open(file_name, 'x', encoding='utf-8') as file:
            return
    except FileExistsError:
        return


class Queue:
    """
    Класс отвечает за работу с очередью запросов.
    """
    queue_file: str = 'queue.txt'

    def __init__(self):
        """
        Создает файл queue.txt, если такового нет в директории с сервером.
        """
        create_file(self.queue_file)

    def check_queue(self) -> str | None:
        """
        Функция проверяет с периодичностью файл queue.txt на наличие запрашиваемых команд.
        Файл queue.txt является хранилищем очереди команд, которые запрашивают клиенты.
        Команды разделены переносом строки. Если файл не пустой, функция возвращает первую строку из queue.txt.
        После извлечения команды, он ее удаляет из файла.
        :return: Первую строку из queue.txt, если он не пустой. Иначе - None.
        """
        first_command: str = ''
        rest_commands: str = ''
        empty_file: bool = True

        # Файл может быть открыт клиентом, поэтому пытаемся его открыть, пока не откроем
        while True:
            try:
                with open(self.queue_file, 'r', encoding='utf-8') as queue:
                    data: str = queue.read()
                    commands: list[str] = data.split('\n')
                    print(commands)

                    if data:
                        first_command += commands[0]
                        rest_commands += '\n'.join(commands[1:])
                        empty_file = False
            except IOError:
                time.sleep(0.1)
            else:
                break
            finally:
                time.sleep(1)  # Засыпаем, чтобы не нагружать процессор

        if empty_file:
            return None
        else:
            # Удалим первую команду из файла
            while True:
                try:
                    with open(self.queue_file, 'w', encoding='utf-8') as queue:
                        queue.write(rest_commands)
                        return first_command
                except IOError:
                    time.sleep(0.1)


class Chat:
    chat_file: str = 'chat.txt'

    def __init__(self):
        create_file(self.chat_file)

    def get_chat_text(self) -> str:
        """
        Функция возвращает полный текст чата. Чат хранится в файле chat.txt в директории сервера.
        :return: Текст чата.
        """
        with open(self.chat_file, 'r', encoding='utf-8') as chat:
            return chat.read()

    def write_new_msg(self, client_name: str, msg: str):
        """
        Метод добавляет новое сообщение
        :param client_name: Имя клиента.
        :param msg: Текст сообщения.
        :return: Ничего.
        """
        print(f'msg = {msg}')
        with open(self.chat_file, 'a', encoding='utf-8') as chat:
            chat.write('{name}: {text}\n'.format(
                name=client_name,
                text=msg
            ))


class Server:
    """
    Класс отвечает за работу сервера.
    """
    users_info_file: str = 'users.txt'  # Будет храниться информация о пользователях

    def __init__(self):
        # Информация о пользователях будет храниться в текстовом файле. Строка будет иметь вид:
        # <id клиента> <имя клиента> <директория, откуда запущен скрипт клиента>\n
        create_file(self.users_info_file)
        self.queue: Queue = Queue()  # Объект очереди
        self.chat: Chat = Chat()  # Объект чата

    def get_user_info(self, client_id: int) -> tuple[str, str]:
        """
        Метод возвращает информацию о клиенте (его имя и директорию).
        :param client_id: id клиента.
        :return: Кортеж из имени и директории клиента
        """
        with open(self.users_info_file, 'r', encoding='utf-8') as users:
            for user in users:
                user_info: list[str] = user.split()
                if int(user_info[0]) == client_id:
                    return user_info[1], user_info[2]

    def send_data_to_client(self, client_id: int, data: str):
        """
        Функция передает запрошенную информацию клиенту. Будет реализована через костыли.
        Сервер будет создавать файл .txt в директории клиента, куда будет сохранять запрошенную информацию.
        Название файла будет иметь вид <id клиента>_True.txt. True добавлен как маркер, который говорит о том, что этот
        файл был изменен сервером и его можно считать. После прочтения клиент изменит название файла на
        <id клиента>_False.txt. False говорит о том, что сервер пока не внес новую информацию в этот файл,
        и клиенту нет необходимости его открывать. При этом, если сервер будет готов отправить сообщение,
        но в директории клиента уже будет файл с названием с маркером True,
        то это будет значить, что клиент еще не успел считать предыдущую информацию. Но для данной задачи,
        это не проблема, так как клиент может запросить только полный текст чата. Сервер будет просто проверять,
        закрыт ли файл с маркером True, и если закрыт - то сервер просто перезапишет информацию.
        :param client_id: id клиента.
        :param data: Запрошенная информация (в данной задаче - текст чата).
        :return: Ничего.
        """
        # Найдем директорию пользователя в users.txt
        user_info: tuple[str, str] = self.get_user_info(client_id)
        user_path: str = user_info[1]
        print(user_path)

        path_false: str = os.path.join(user_path, f'{client_id}_False.txt')
        path_true: str = os.path.join(user_path, f'{client_id}_True.txt')

        # Проверим, есть ли файл <id клиента>_False.txt в директории клиента
        if os.path.exists(path_false):
            # Если он существует, то можем не беспокоиться о том, что кто-то его мог открыть
            with open(path_false, 'w', encoding='utf-8') as file:
                file.write(data)
            # Теперь переименуем файл, изменив маркер на True
            os.rename(path_false, path_true)
        # Иначе проверим существование файла <id клиента>_True.txt
        elif os.path.exists(path_true):
            # Если есть - будем пробовать его открыть, пока не откроем
            while True:
                try:
                    with open(path_true, 'w', encoding='utf-8') as file:
                        file.write(data)
                except IOError:
                    time.sleep(0.2)  # Нужно, чтобы не нагружать процессор
                else:
                    break
        # Если не найдены никакие файлы, значит их еще нет - создадим их
        else:
            with open(path_true, 'w', encoding='utf-8') as file:
                file.write(data)

    def write_new_msg(self, client_id: int, msg: str):
        """
        Метод записывает новое сообщение в чат.
        :param client_id: id клиента.
        :param msg: Текст сообщения.
        :return: Ничего.
        """
        # Найдем имя пользователя
        user_info: tuple[str, str] = self.get_user_info(client_id)
        user_name: str = user_info[0]

        # Запишем новое сообщение
        self.chat.write_new_msg(client_name=user_name, msg=msg)

    def loop(self):
        """
        Метод отвечает за основную работу сервера.
        Метод будет работать в бесконечном цикле.
        :return: Ничего.
        """
        while True:
            # 1) Получим команду из очереди
            command: str | None = self.queue.check_queue()
            while command is None:
                time.sleep(0.1)  # Нужно, чтобы не нагружать процессор при пустой очереди
                command: str | None = self.queue.check_queue()

            # Команда имеет вид: <id клиента> <id команды> <текст сообщения (необязательно)>\n
            command_info: list[str] = command.split()
            client_id: int = int(command_info[0])
            command_id: int = int(command_info[1])
            msg: str = ''
            if len(command_info) >= 3:
                msg += ' '.join(command_info[2:])

            # Команда 1 - получить текст чата.
            # Команда 2 - написать новое сообщение.
            if command_id == 1:
                self.send_data_to_client(
                    client_id=client_id,
                    data=self.chat.get_chat_text()
                )
            elif command_id == 2:
                self.write_new_msg(client_id=client_id, msg=msg)


server: Server = Server()
server.loop()
