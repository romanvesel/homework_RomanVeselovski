x = int(input('Enter number: '))
total = 0
new_list2 = []
compos = 1
if len(str(x)) < 2:
    print(x)
else:
    new_list = list(str(x))
    for el in new_list:
        new_list2.append(int(el))
        total = sum(new_list2)
    for x in new_list2:
        compos = x * compos

    print(total)
    print(compos)
