#us = int(input('Что вы хотите сделать? (добавить расход (1) /  / посмотреть все расходы (2) / сумма расходов и средний расход (3) / удалить расход по номеру (4)): '))
list_of_expenses = []
while True:
    us = input('Что вы хотите сделать? (добавить расход (1) / посмотреть все расходы (2) / сумма расходов и средний расход (3) / удалить расход по номеру (4) / выйти из приложения (5)): ')
    if us == '1':
        exp = float(input('Введите расход: '))
        list_of_expenses.append(exp)
    if us == '2':
        print(f'Все расходы: {list_of_expenses}')
    if us == '3':
        print(f'Сумма расходов: {sum(list_of_expenses)}')
        print(f'Средний расход: {sum(list_of_expenses / len(list_of_expenses))}')
    if us == '4':
        us_num = int(input('введите номер расхода: '))
        if us_num in range(0, len(list_of_expenses) + 1):
            list_of_expenses.remove(list_of_expenses[us_num])
            print(f'Все расходы: {list_of_expenses}')
        else:
            print('Нет такого значения')
    if us == '5':
        break
