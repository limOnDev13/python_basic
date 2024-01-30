shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail_name: str = input('Название детали: ')

num_details: int = 0
total_price: int = 0

for product in shop:
    if product[0] == detail_name:
        num_details += 1
        total_price += product[1]

print('Кол-во деталей -', num_details)
print('Общая стоимость -', total_price)
