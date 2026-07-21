price = int(input("Введите цену товара: "))
discount = int(input("Введите процент скидки: "))
total = price - (price * (discount / 100))
print(f"Цена со скидкой: {total} руб.")