'''
При рассмотрении простейших операций со строками было показано, как
объединять строки с помощью операции сложения. Другую возможность для
соединения строк представляет метод join(): он объединяет список строк.
Причем текущая строка, у которой вызывается данный метод, используется в
качестве разделителя:
'''

words = ["Let", "me", "speak", "from", "my", "heart", "in", "English"]

# разделитель - пробел
sentence = " ".join(words)
print(sentence)  # Let me speak from my heart in English

# разделитель - вертикальная черта
sentence = " | ".join(words)
print(sentence)  # Let | me | speak | from | my | heart | in | English



'''
Вместо списка в метод join можно передать простую строку, тогда разделитель 
будет вставляться между символами этой строки:
'''

word = "hello"
joined_word = "|".join(word)
print(joined_word)      # h|e|l|l|o