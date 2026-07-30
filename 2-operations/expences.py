eat = int(input("Введите сумму расхода на еду: "))
transport = int(input("Введите сумму расхода на транспорт: "))
fun = int(input("Введите сумму расхода на развлечения: "))
total = eat + transport + fun
average =  (eat + transport + fun) / 3
print(f"Общий расход: {total} руб.")
print(f"Средний расход: {average} руб.")