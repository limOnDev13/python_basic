def smallest_divisor(number: int) -> int:
    for num in range(2, number + 1):
        if number % num == 0:
            return num


n: int = int(input('Введите число: '))

print('Наименьший делитель, отличный от единицы:', smallest_divisor(n))
