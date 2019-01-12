word = input("type a word for checking so checking palindrome or not:")
word_len = len(word)    # length of your input string
reverse_word = ""
while word_len != 0:    # while we don't achieve to the beginning of input string
    reverse_word = reverse_word + word[word_len-1]     # Add last character to reverse_word
    word_len = word_len - 1      # change index to the next digit
if reverse_word == word:
    print('Palindrome')
else:
    print('Not Palindrome')