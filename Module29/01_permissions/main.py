from typing import Iterator, Literal, TextIO, Optional
from contextlib import contextmanager


@contextmanager
def file(name: str, mode: Literal['r', 'w', 'a']) -> Iterator:
    required_file: Optional[TextIO] = None

    try:
        required_file = open(name, mode, encoding='utf-8')
        yield required_file
    except FileNotFoundError:
        yield open(name, 'w', encoding='utf-8')
    except Exception as exc:
        print(exc)
    finally:
        if required_file is not None:
            required_file.close()


with file('test_file.txt', 'w') as f:
    f.write()

print('Код все еще работает...')
