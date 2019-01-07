year = int(input("insert year:"))
print(year.isalpha())

if year > 0:
    century = year/100
    if century % int(century)== 0:
      print(int(century),'th century')
    else:
      print(int(century + 1),'th century')
#elif year != re.match('^[A-Za-z ]*$'):
    print('string')

else:
    print('Wrong value')

