import datetime
#choice = 'y'

#while choice.lower() == "y":
#    print("Привет")
#    choice = input("Для продолжения нажмите Y, а для выхода любую другую клавишу: ")
#print("Работа программы завешена")

#now = datetime.datetime.now()
#while now.time().minute == int(29):
#    print('Sasoooo')


# ! Программа по вычислению факториала

number = int(input("Введите число: "))
i = 1
factorial = 1
while i <= number:
    factorial *= i
    i += 1
print("Факториал числа", number, "равен", factorial)