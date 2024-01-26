def sum_nums(number: int) -> int:
    result_sum: int = 0

    for sym in str(number):
        result_sum += int(sym)

    return result_sum


def amount_nums(number: int) -> int:
    result_amount: int = len(str(number))
    return result_amount


n: int = int(input('Введите число: '))
sum_numbers: int = sum_nums(n)
amount_numbers: int = amount_nums(n)

print()
print('Сумма цифр:', sum_numbers)
print('Количество цифр в числе:', amount_numbers)
print('Разность суммы и количества цифр:', sum_numbers - amount_numbers)
