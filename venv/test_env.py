def centuryFromYear(year):
    year = (year - 1) / 100 + 1
    print(int(year))


year = 45
centuryFromYear(year)
year = 1700
centuryFromYear(year)