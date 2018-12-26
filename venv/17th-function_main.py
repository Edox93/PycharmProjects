'''Функция main
В программе может быть определено множество функций.
И чтобы всех их упорядочить, хорошей практикой считается
добавление специальной функции main, в которой потом уже
вызываются другие функции:'''

def main():
    say_hello("Edgar")
    usd_rate = 485.5
    money = 30000
    result = exchange(usd_rate, money)
    print("К выдаче", result, "долларов")


def say_hello(name):
    print("Hello,", name)


def exchange(usd_rate, money):
    result = round(money / usd_rate, 2)
    return result


# Вызов функции main
main()