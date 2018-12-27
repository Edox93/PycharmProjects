rate = 2
money = 10
month = 3
for i in range(1, month + 1):
    money = round(money + money * rate / 100 / 12, 2)

print( round(money, 2))
