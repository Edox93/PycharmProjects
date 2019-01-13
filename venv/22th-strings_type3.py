'''   Для поиска подстроки в строке в Python применяется метод find(), который возвращает индекс первого вхождения подстроки в строку и имеет три формы:
find(str): поиск подстроки str ведется с начала строки до ее конца
find(str, start): параметр start задает начальный индекс, с которого будет производиться поиск
find(str, start, end): параметр end задает конечный индекс, до которого будет идти поиск
Если подстрока не найдена, метод возвращает -1:   '''


word = "alexandrapol"
found_word_or_substring = word.find('exa')
print(found_word_or_substring)  # 2

# поиск с 10-го индекса
index = welcome.find("wor", 10)
print(index)  # 21

# поиск с 10 по 15 индекс
index = welcome.find("wor", 10, 15)
print(index)  # -1

'''
Для замены в строке одной подстроки на другую применяется метод replace():
replace(old, new): заменяет подстроку old на new
replace(old, new, num): параметр num указывает, сколько вхождений подстроки 
old надо заменить на new  '''

phone = "+1-234-567-89-10"

# замена дефисов на пробел
edited_phone = phone.replace("-", " ")
print(edited_phone)  # +1 234 567 89 10

# удаление дефисов
edited_phone = phone.replace("-", "")
print(edited_phone)  # +12345678910

# замена только первого дефиса
edited_phone = phone.replace("-", "", 1)
print(edited_phone)  # +1234-567-89-10


'''
Метод split() разбивает строку на список подстрок в зависимости от 
разделителя. В качестве разделителя может выступать любой символ или 
последовательность символов. Данный метод имеет следующие формы:
split(): в качестве разделителя используется пробел
split(delimeter): в качестве разделителя используется delimeter
split(delimeter, num): параметр num указывает, сколько вхождений delimeter 
используется для разделения. Оставшаяся часть строки добавляется в список 
без разделения на подстроки
'''

text = "Это был огромный, в два обхвата дуб, с обломанными ветвями и с обломанной корой"
# разделение по пробелам
splitted_text = text.split()
print(splitted_text)
print(splitted_text[6])  # дуб,

# разбиение по запятым
splitted_text = text.split(",")
print(splitted_text)
print(splitted_text[1])  # в два обхвата дуб

# разбиение по первым пяти пробелам
splitted_text = text.split(" ", 5)
print(splitted_text)
print(splitted_text[5])  # обхвата дуб, с обломанными ветвями и с обломанной корой


