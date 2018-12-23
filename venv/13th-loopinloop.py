#Loop FOR, when '\n' is in 2nd loop
for i in range(1, 5):
    for j in range(1, 5):
        print(i * j, end='\t')
        print("\n")

print('2nd case')

#Loop FOR, when '\n' is in 1st loop
for i in range(1, 5):
    for j in range(1, 5):
        print(i * j, end='\t')
    print("\n")

print('3th case')

#Loop FOR, when '\n' is out the loop
for i in range(1, 5):
    for j in range(1, 5):
        print(i * j, end='\t')
print("\n")