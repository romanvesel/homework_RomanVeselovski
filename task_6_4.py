from random import randint

summa = 0
a = int(input('Enter a: '))
b = int(input('Enter b: '))
n = int(input('Enter n: '))
m = int(input('Enter m: '))
matrix = [[randint(a, b) for i in range(n)] for j in range(m)]

for value in matrix:
    summa += sum(value)

print(summa)
print(matrix)
