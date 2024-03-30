from typing import TextIO, Optional, Literal


class File:
    """
    Контекст-менеджер для работы с файлами.

    Args:
        file_name (str) - Имя открываемого файла
        mode (Literal['w', 'r', 'a']) - Режим открытия файла
    """
    def __init__(self, file_name: str, mode: Literal['w', 'r', 'a']) -> None:
        self.__name: str = file_name
        self.__mode: Literal['w', 'r', 'a'] = mode
        self.__file: Optional[TextIO] = None

    def __enter__(self) -> TextIO:
        """Если файл не существует, то он будет создан автоматически."""
        self.__file = open(self.__name, self.__mode, encoding='utf-8')
        return self.__file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """При выходе из контекстного менеджера будут подавляться все исключения"""
        self.__file.close()
        return True


# Проверка
with File('test_task_1.txt', 'w') as file:
    # Запишем не строку, чтобы было исключение
    file.write(1)

print('Код все еще работает')
