# TODO здесь писать код
number: int = int(input('Введите число: '))

res_numbers = [num for num in range(1, number + 1, 2)]
print('Список из нечетных чисел от одного до N:', res_numbers)
