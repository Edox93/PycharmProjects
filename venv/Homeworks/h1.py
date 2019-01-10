def ed_loop(digit):
    for i in range(1, digit + 1):
        if i % 2 == 0:
            print(int(i))


digit = int(input('sum:'))
ed_loop(digit)
print('the number of even numbers is :', int(digit // 2))




