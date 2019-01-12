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

'''def centuryFromYear(year):
    year = year/100
    if year < 100:
       year = (year / 100 + 1)
       print(int(year))
    else:
        if year % int(year) == 0:
            print(int(year))
        else:
            print(int(year + 1))

year = 1500
centuryFromYear(year)'''

#----------------------------------
'''def centuryFromYear(year):
    if year % 100 == 0:
        return int(year / 100)
    else:
        return int(year / 100 + 1)

while 1 > 0:
    print(centuryFromYear(int(input())))'''