#!Logical Operators and, or, not
# in the same function or object they works by priority
#1st:not 2nd:and 3th:or

#AND
age = 25
weight = 76
result = age < 0 and weight == age
print(result)

age = 25
height = 155
isEngaged = False
report = age < 30 and height > age and isEngaged < True
print(report)
print('\n')

#OR
age = 25
weight = 76
result = age < 0 or weight > age
print(result)

age = 25
height = 155
isEngaged = False
report = age < 30 or height > age or isEngaged < False
print(report)
print('\n')

#NOT
age = 22
isMarried = False
print(not age > 21)  # False
print(not isMarried)  # True
print('\n')
age = 25
height = 155
isEngaged = False
report = age < 30 or height > age or isEngaged < False
print(not report)
print('\n')





age = 22
isMarried = False
weight = 58
result = weight == 58 or isMarried and not age > 21  # True
print(result)  #True  OR    ( False        False )

age = 22
isMarried = False
weight = 58
result = weight == 58 and not age > 21  # False
print(result) #Trune  #AND   #False


#Для переопределения порядка вычислений мы можем использовать скобки:
age = 22
isMarried = False
weight = 58
result = (weight == 58 or isMarried) and not age > 21  # False
print(result)     #True              #AND   #False


age = 22
isMarried = False
weight = 58
result = (weight == 58) and not age > 21  # False
print(result) #True     #AND    #Flase

