file_name: str = input('Название файла: ')

start_error: str = '*@№$%^&()\\'

if file_name[0] in start_error:
    print('Ошибка: название начинается на один из специальных символов.')
elif not file_name.endswith('.txt') and not file_name.endswith('.docx'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')
