kids = int(input('number of kids:'))
cakes = int(input('number of cakes:'))

d = cakes % kids
cakes = cakes - d
e = cakes / kids

print(int(e))