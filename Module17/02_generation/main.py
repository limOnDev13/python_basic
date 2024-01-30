n: int = int(input('Введите длину списка: '))

print('Результат:', [(1 if num % 2 == 0 else num % 5) for num in range(n)])
