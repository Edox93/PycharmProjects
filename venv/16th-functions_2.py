def sum(*params):
    result = 0
    for n in params:
        result += n
    return result


sumOfNumbers1 = sum(1, 2, 3, 4, 5)  # 15
sumOfNumbers2 = sum(3, 4, 5, 6)  # 18
print(sumOfNumbers1)
print(sumOfNumbers2)

###########################################

def sum(*params):
    result = 1
    for n in params:
        result *= n
    return result


multiplicationOfNumbers1 = sum(1, 2, 3, 4, 5)  # 120
multiplicationOfNumbers2 = sum(3, 4, 5, 6)  # 360
print(multiplicationOfNumbers1)
print(multiplicationOfNumbers2)

print(' \n')
##################################################
def exchange(usd_rate, money):
    result = round(money / usd_rate, 2)
    return result

result1 = exchange(485, 10000)
print(result1)
result2 = exchange(485.5, 10000)
print(result2)
result3 = exchange(486, 10000)
print(result3)

print('\n')
###############################################
def create_default_user():
    name = "Edgar"
    age = 25
    dob = '02.03.1993'
    return name, age, dob


user_name, user_age, user_dob = create_default_user()
print("Name:", user_name, "\nAge:", user_age, "\nD.O.B.:", user_dob)