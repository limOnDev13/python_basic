ip_address: str = input('Введите IP: ')

numbers: list[str] = ip_address.split('.')
# Контроль количества
if len(numbers) != 4:
    print('Адрес — это четыре числа, разделённые точками.')
    exit()

# Контроль типа данных и их корректность
for num in numbers:
    if not num.isdigit():
        print('{} - это не целое число.'.format(num))
        break
    elif int(num) < 0:
        print('{} меньше 0'.format(num))
        break
    elif int(num) > 255:
        print('{} превышает 255.'.format(num))
        break
else:
    print('IP-адрес корректен.')
