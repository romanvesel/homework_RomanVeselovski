def fact(n):
    if n % 2 == 0:
        length = list(range(1, n))
        for i in length:
            if i % 2 == 0:
                n *= i
        print(n)
    else:
        length = list(range(1, n))
        for i in length:
            if i % 2 == 1:
                n *= i
        print(n)
# n = int(input('Enter number: '))
# fact(n)



some_list = [2, 4, 9, 5, 7]
for value in some_list:
    fact(value)
