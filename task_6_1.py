from random import randint
#
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# n = int(input('Enter n: '))
# m = int(input('Enter m: '))
# matrix = [[randint(a, b) for i in range(n)] for j in range(m)]
# print(matrix)
#
#
#
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# n = int(input('Enter n: '))
# m = int(input('Enter m: '))
# matrix = [[randint(a, b) for i in range(n)] for j in range(m)]
# max_el = max(max(matrix))
# print(max_el)


# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# n = int(input('Enter n: '))
# m = int(input('Enter m: '))
# matrix = [[randint(a, b) for i in range(n)] for j in range(m)]
# min_el = min(min(matrix))
# print(min_el)

summa = 0
a = int(input('Enter a: '))
b = int(input('Enter b: '))
n = int(input('Enter n: '))
m = int(input('Enter m: '))
matrix = [[randint(a, b) for i in range(n)] for j in range(m)]
for x in matrix:
    summa += sum(x)
print(summa)
print(matrix)


