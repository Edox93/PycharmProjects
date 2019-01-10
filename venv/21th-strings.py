zoro = "Zoro Chlomkes"
print(zoro[6])
print(zoro[0])
print(zoro[5] + zoro[6] + zoro[8] + zoro[2])
print('\n')
print(zoro[:3])
print(zoro[1:6])
print(zoro[1:6:2]) #from index1 to index 6, every 2nd symbol

print('\n')
edox = 'karakal'
if edox[1] == edox[-2]:
    print('matched')
else:
    print('not matched')

print('\n')

print(ord('A')) #65
print(ord('a')) #97
print(ord('B')) #66
print(ord('b')) #98
print(ord('Z')) #90 prining The number of unicode letter
print(ord('z')) #122
print(len('Zoro')) #4 prining The length of unicode letter/string
print('\n')

boc = 'zoro chlomkes'
exist = 'zoro' in boc
print(exist)   #True  checking substring that exist or not

boc = 'tea coffee'
exist = 'coffee' in boc
print(exist)    #True
exist = 'gago' in boc
print(exist)    #False




