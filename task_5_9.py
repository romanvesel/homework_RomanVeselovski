n = int(input('Enter first number: '))
m = int(input('Enter second number: '))
some_list = list(range(n, m+1))



for i, j in enumerate(some_list):
    counter = 0
    div = []
    while counter < j:
        counter += 1
        if some_list[i] % counter == 0:
            div.append(counter)
    print(f'Число: {j} \n{div[1:-2]}\n')
    # print(div)

# print(f'Массив данных: {some_list}')