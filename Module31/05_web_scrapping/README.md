## Задача 5. Web scraping
### Что нужно сделать
Дан несложный пример HTML-страницы: [Sample Web Page](https://www.columbia.edu/~fdc/sample.html)<br>
Изучите код этой страницы и реализуйте программу, которая получает список всех подзаголовков сайта (они заключены в теги `<h3>`).

В качестве альтернативы [сайту](https://www.columbia.edu/~fdc/sample.html) служит файл  `examples.html`

Ожидаемый результат:
```python
# Для https://www.columbia.edu/~fdc/sample.html
['CONTENTS',
 '1. Creating a Web Page',
 '2. HTML Syntax',
 '3. Special Characters',
 '4. Converting Plain Text to HTML',
 '5. Effects',
 '6. Lists',
 '7. Links',
 '8. Tables', 
 '9. Viewing Your Web Page', 
 '10. Installing Your Web Page on the Internet',
 '11. Where to go from here',
 '12. Postscript: Cell Phones'
 ]

# Для файла examples.html
['Latest News', 'Useful Links', 'Search', 'Heading 3']
```

Сделайте так, чтобы программа работала для любого сайта, где есть такие теги.

Дополнительно:
найдите любой сайт, у которого в коде есть теги 'h3', выполните get-запрос к этому сайту при помощи библиотеки requests и получите аналогичный список всех его подзаголовков (заключенных в теги 'h3')


### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Решение опирается на использование регулярных выражений и их методов.
- Переменные, функции и собственные методы классов имеют значащие имена, не `a`, `b`, `c`, `d`.
