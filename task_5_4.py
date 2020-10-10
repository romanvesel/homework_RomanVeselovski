nat_numb = int(input('Введите натуральное число: '))
new_list = list(range(1, nat_numb+1))
total = 0
for i in new_list:
    i = nat_numb / i
    total += i
    print(i)

print(f'Cумма = {total}')