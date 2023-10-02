age=int(input("Введите возраст:"))
name=(input("Введите имя:"))
if age>0 and age<75:
    if not "Иван" in name:
        if age>=16:
            print("Поздравляем вы поступили в ВГУИТ")
        else:
            print("Сначала нужно окончить школу")
            print("Остаток лет учёбы в школе:",(16-age))
            