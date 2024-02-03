text: str = input('Введите строку: ')

words: list[str] = text.split()
largest_word: str = max(words, key=lambda x: len(x))

print('Самое длиное слово: {word}\nДлина этого слова: {length}'.format(
    word=largest_word,
    length=len(largest_word)
))
