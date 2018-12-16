#! Программа Обменный пункт

usd = 483
euro = 545

money = int(input("Введите сумму, которую вы хотите обменять: "))
currency = int(input("Укажите код валюты (доллары - 10, евро - 20): "))

if currency == 10:
    cash = round(money / usd, 2)
    print("Валюта: доллары США")
elif currency == 20:
    cash = round(money / euro, 2)
    print("Валюта: евро")
else:
    cash = 0
    print("Неизвестная валюта")

print("К получению:", cash)