s = input().lower().strip()

s = s.replace("рублей", "руб")
s = s.replace("руб.", "руб")
s = s.replace("копеек", "коп")
s = s.replace("коп.", "коп")

parts = s.split()

if len(parts) == 2:
    if parts[1] == "руб" and parts[0].isdigit():
        rub = int(parts[0])
        kop = 0
        print("{:.2f} ₽".format(rub + kop / 100))
    else:
        print("Некорректный формат суммы")

elif len(parts) == 4:
    if (
        parts[1] == "руб"
        and parts[3] == "коп"
        and parts[0].isdigit()
        and parts[2].isdigit()
    ):
        rub = int(parts[0])
        kop = int(parts[2])
        print("{:.2f} ₽".format(rub + kop / 100))
    else:
        print("Некорректный формат суммы")

else:
    print("Некорректный формат суммы")