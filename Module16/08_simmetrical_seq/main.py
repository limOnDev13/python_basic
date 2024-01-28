amount_nums: int = int(input('Кол-во чисел: '))

init_list: list[int] = list()
for _ in range(amount_nums):
    num: int = int(input('Число: '))
    init_list.append(num)

reversed_list: list[int] = init_list[::-1]

# Логика простая. Мы из каждого (i + delta)-го элемента init_list
# вычитаем i-й элемент reversed_list, где delta - смещение массивов
# относительно друг друга. Если в какой-то момент все такие разности
# будут равны 0, то мы нашли симметричную часть, => остается к init_list
# прибавить смещенную часть reversed_list:
result_delta: int = 0

for delta in range(len(init_list)):
    for index in range(0, len(reversed_list) - delta):
        if init_list[index + delta] - reversed_list[index] != 0:
            break
    else:
        result_delta = delta
        break

print('Последовательность:', init_list)
print('Нужно приписать чисел:', result_delta)
print('Сами числа:', reversed_list[amount_nums - result_delta::])
