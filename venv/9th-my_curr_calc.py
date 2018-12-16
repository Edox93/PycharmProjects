

rub = 7.22
usd = 483.5
euro = 545
gbp = 604

money = int(input('input money in Armenian drams to converting'))
currency = int(input('input currency, rub=1, usd=2, euro=3, gbp=4 '))

if currency == 1:
    result = money / rub
    print('RF Rublies')
elif currency == 2:
    result = money / usd
    print('USA Dollars')
elif currency == 3:
    result = money / euro
    print('European euros')
elif currency == 4:
    print('GB phunds')
else:
    result = 'Wrong'
    print('wrong currency')
print('The result is', result)

