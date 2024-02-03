text: str = input('Введите строку: ')

left_h_index: int = text.index('h')
right_h_index: int = text.rindex('h')

print('Развернутая последовательность между первым и последним h:', text[right_h_index - 1:left_h_index:-1])
