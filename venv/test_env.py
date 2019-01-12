string = input('type digit in this input so checking type is int or not')
if string.isnumeric():
    string = int(string)
    print(string)
else:
    print("The input isn't integer ")

