'''
range(stop): возвращает все целые числа от 0 до stop

range(start, stop): возвращает все целые числа в промежутке
от start (включая) до stop (не включая). Выше в программе
факториала использована именно эта форма.

range(start, stop, step): возвращает целые числа в промежутке
от start (включая) до stop (не включая), которые
увеличиваются на значение step

Примеры вызовов функции range:

range(5)            # 0, 1, 2, 3, 4
range(1, 5)         # 1, 2, 3, 4
range(2, 10, 2)     # 2, 4, 6, 8
range(5, 0, -1)     # 5, 4, 3, 2, 1
'''

for i in range(5):
    print(i, end=" ", )

print('\n')
for i in range(5):
    print(i)

print('\n')
for i in range(1, 10):
    for j in range(1,10):
        print(i * j, end="\t")
    print("\n")
