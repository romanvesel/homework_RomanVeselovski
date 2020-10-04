lst = [1, 2, 3, 4]
new_lst = []
for i in lst:
    new_lst.append(i*-2)
print(new_lst)

print('---------------------------------')


while True:
    lst[0] *= -2
    lst[1] *= -2
    lst[2] *= -2
    lst[3] *= -2
    new_lst2 = lst[0:]
    if lst[3] > 5:
        break
    print(new_lst2)