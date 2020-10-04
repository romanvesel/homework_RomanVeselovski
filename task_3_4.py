some_str = input('Enter some text: ')
length_some_str = int(len(some_str))
half_of_str = int(length_some_str / 2)
middle_symbol = some_str[half_of_str]
if half_of_str % 2 == 0:
    middle_symbol = some_str[half_of_str]
    print (middle_symbol)
elif half_of_str % 2 != 0:
    middle_symbol = some_str[half_of_str]
    print (middle_symbol)
if middle_symbol == some_str[0]:
    print (some_str[1:-1])
