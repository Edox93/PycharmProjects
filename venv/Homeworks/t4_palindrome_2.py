word = input("type a word for checking so checking palindrome or not:")
reverse_word = word[::-1]
if reverse_word == word:
    print('Palindrome')
else:
    print('Not Palindrome')

