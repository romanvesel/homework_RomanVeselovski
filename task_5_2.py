x = int(input('Enter number: '))
total = 0
new_list2 = []

if len(str(x)) < 2:
    print(x)
else:
    new_list = list(str(x))
    for el in new_list:
        new_list2.append(int(el))
        total = sum(new_list2)

    print(total)
