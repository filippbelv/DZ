category = input("Выберите категорию (напиток/суп/десерт): ")

match category:
    case "напиток":
        print("Варианты: чай, кофе, сок")
        drink = input("Выберите напиток: ")
        match drink:
            case "чай":
                print("Цена: 50 руб")
            case "кофе":
                print("Цена: 100 руб")
            case "сок":
                print("Цена: 80 руб")
    case "суп":
        print("Варианты: борщ, щи, суп-пюре")
        soup = input("Выберите суп: ")
        match soup:
            case "борщ":
                print("Цена: 200 руб")
            case "щи":
                print("Цена: 250 руб")
            case "суп-пюре":
                print("Цена: 400 руб")
    case "десерт":
        print("Варианты: торт, мороженое, фрукты")
        desert = input("Выберите десерт: ")
        match desert:
            case "торт":
                print("Цена: 250 руб")
            case "мороженое":
                print("Цена: 200 руб")
            case "фрукты":
                print("Цена: 500 руб")