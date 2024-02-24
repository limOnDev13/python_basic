import re


def read_lines(input_file: str = 'registrations.txt') -> list[str]:
    """
    Функция считывает информацию из файла построчно.
    :param input_file: Имя файла с информацией.
    :return: Список строк.
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        return file.read().split('\n')


def write_logs(persons_info: list[str],
               good_logs_file: str = 'registrations_good.log',
               bad_logs_file: str = 'registrations_bad.log'):
    """
    Функция записывает плохие и хорошие логи согласно условию задачи.
    :param persons_info: Список строк с информациями о людях.
    :param good_logs_file: Имя файла с хорошими логами.
    :param bad_logs_file: Имя файла с плохими логами.
    :return: Ничего.
    """
    with (open(good_logs_file, 'w', encoding='utf-8') as good_logs,
          open(bad_logs_file, 'w', encoding='utf-8') as bad_logs):
        for info in persons_info:
            try:
                if len(info.split()) != 3:
                    raise IndexError('НЕ присутствуют все три поля')

                fields: list[str] = info.split()
                if not fields[0].isalpha():
                    raise NameError('Поле «Имя» содержит НЕ только буквы')
                if not re.match('.+@.+[.].+', fields[1]):
                    raise SyntaxError('Поле «Имейл» НЕ содержит @ и . (точку)')
                if not (fields[2].isdigit() and 10 <= int(fields[2]) <= 99):
                    raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')
            except (IndexError, NameError, SyntaxError, ValueError) as exc:
                bad_logs.write(f"{info}{'\t' * 4}{str(exc)}\n")
            else:
                good_logs.write(f'{info}\n')


write_logs(read_lines())
