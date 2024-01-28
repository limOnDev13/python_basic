# TODO здесь писать код

# Список чисел для работы (итоговый алгоритм проверьте на разных списках, придуманных самостоятельно):
numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]
print('Список чисел:', numbers_list)

for i in range(0, -len(numbers_list), -1):
    if numbers_list[i] % 2 == 0:
        print(numbers_list[i], end='\t')
