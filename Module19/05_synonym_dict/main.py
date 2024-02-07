def get_synonym(dictionary: dict[str, str], word: str
                ) -> str | None:
    """
    Функция ищет в словаре dictionary (как по ключам,
     так и по значениям) слово word и возвращает его пару.
    :param dictionary: Список синонимов.
    :param word: Искомое слово.
    :return: Если word есть в dictionary, то его синоним.
    Если нет - None
    """
    # Приведем все слова в словаре к маленькому регистру
    if word in dictionary:
        return dictionary[word]
    elif word in dictionary.values():
        for first_word, second_word in dictionary.items():
            if second_word == word:
                return first_word
    else:
        return None


num_pairs: int = int(input('Введите количество пар слов: '))
pairs: list[list[str]] = [
    input('{} пара: '.format(index)).split(' — ')
    for index in range(1, num_pairs + 1)
]
synonyms: dict[str, str] = {
    pair[0]: pair[1]
    for pair in pairs
}

# Будем спрашивать пользователя, пока он не введет слово из словаря
synonym: str | None = get_synonym(
    dictionary=synonyms,
    word=input('Введите слово: ').lower()
)
while synonym is None:
    print('Такого слова в словаре нет.')
    synonym = get_synonym(
        dictionary=synonyms,
        word=input('Введите слово: ').lower()
    )
print('Синоним:', synonym)
