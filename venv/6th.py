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

#!Strings

name = "Tom"
surname = 'Smith'
print(name, surname)  # Tom Smith

#merg streing in one
name = "Tom"
surname = 'Smith'
fullname = name + " " + surname
print(fullname)  # Tom Smith

#str(): converting int to string
name = "Tom"
age = 33
info = "Name: " + name + " Age: " + str(age)
print(info)  # Name: Tom Age: 33


# \n \t
print("Кафе \n Central Perk")
#   Кафе
#    Central Perk

print("Кафе \"Central Perk\"")   #Кафе "Central Perk"

#compairing strings
str1 = '1a' #priority1 digit
str2 = 'aa' #priority2 under register
str3 = 'Aa' #Priority3

str5 = 'aa' #priority1 first register
str6 = 'ba' #Priority2 second

#lower() приводит строку к нижнему регистру,
#upper() - к верхнему.
str1 = "Tom"
str2 = "tom"
print(str1 == str2)  # False - строки не равны
print(str1.lower() == str2)  # True
print(str2.upper() == str1.upper())  # True
