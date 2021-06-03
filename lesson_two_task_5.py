'''
Создать вручную список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]
Вывести на экран эти цены через запятую в одну строку, цена должна отображаться
в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить
рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

'''


price_list = [57.8, 46.51, 97, 34, 212.32, 5.4, 1.2, 5.9]

new_price = []

for numb in price_list:
    numbs = float(numb)
    str_one = str(numbs)
    a, b = map(int, str_one.split('.'))
    new_list = f'{a:02d} руб {b:02d} коп'
    new_price.append(new_list)
print(new_price)