string = input('type digit in this input so checking type is int or not')
if string.isnumeric():
    string = int(string)
    print(string)
else:
    print("The input isn't integer ")



word = input('write a string:')
starts_with_substring = word.startswith("hello")   # if start is substring than return True
ends_with_substring = word.endswith("exe")           # if end is substring than return True


# Удаление пробелов в начале и в конце строки:
string = "   hello  world!  "
string = string.strip()
print(string)           # hello  world!

# Дополнение строки пробелами и выравнивание:
print("iPhone 7:", "52000".rjust(10))  # iPhone 7:      52000
print("Huawei P10:", "36000".rjust(10)) # Huawei P10:      36000






