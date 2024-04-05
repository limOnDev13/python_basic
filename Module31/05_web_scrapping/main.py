import re
import requests


def find_tag(html_text: str, tag: str = 'h3') -> list[str]:
    """
    Функция ищет текст, заключенный между открывающимся и закрывающимся тегами tag
    :param html_text: html код в виде одной строки
    :type html_text: str
    :param tag: Имя тега
    :type tag: str
    :return: Список строк, которые заключены в данный тег
    :rtype: list[str]
    """
    # Соберем паттерн регулярного выражения
    pattern: str = r'<{tag}.*>.*</{tag}>'.format(tag=re.escape(tag))

    # Найдем все подстроки по этому шаблону
    required_strings: list[str] = re.findall(pattern, html_text)

    # Так как required_string содержит не только тексты, но и тег, то удалим теги и вернем списки
    for index, string in enumerate(required_strings):
        string = re.sub(r'<{tag}.*>\b'.format(tag=tag), '', string)
        string = re.sub(r'</{tag}>'.format(tag=tag), '', string)
        required_strings[index] = string

    return required_strings


if __name__ == '__main__':
    # В данном случае запрос request.get заменен на загрузку сайта из файла html
    print('Пример с examples.html')
    with open('examples.html', 'r') as f:
        text = f.read()
        print(find_tag(text))
    # По итогу вы так же получаете код сайта в виде одной строки

    print('Пример с сайтом https://www.columbia.edu/~fdc/sample.html')
    html_code: str = requests.get('https://www.columbia.edu/~fdc/sample.html').text
    print(find_tag(html_code))
