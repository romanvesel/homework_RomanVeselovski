from random import randint

n = int(input('Enter size:'))
m = n
some_list =[]

matrix = [[randint(1, 100) for j in range(n)] for i in range(m)]
print(f'Начальная матрица:  {matrix}')

for value in matrix:
    h = max(value)
    some_list.append(h)

highest = max(some_list)

for index, numb in enumerate(matrix):
    matrix[0 + index][0 + index] = highest
print(f'Измененная матрица: {matrix}')
print(f'Максимальный элемент матрицы = {highest}')
