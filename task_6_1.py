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
# list_max_el = []
# matrix = [[randint(a, b) for i in range(n)] for j in range(m)]
# for index, value in enumerate(matrix):
#     max_el = max(matrix[index])
#     list_max_el.append(max_el)
# print(max(list_max_el))
# print(matrix)



# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# n = int(input('Enter n: '))
# m = int(input('Enter m: '))
# list_min_el = []
# matrix = [[randint(a, b) for i in range(n)] for j in range(m)]
# for index, value in enumerate(matrix):
#     min_el = min(matrix[index])
#     list_min_el.append(min_el)
# print(min(list_min_el))
# print(matrix)



# sum_list = []
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# n = int(input('Enter n: '))
# m = int(input('Enter m: '))
# matrix = [[randint(a, b) for i in range(n)] for j in range(m)]
# for i, j in enumerate(matrix):
#     sum_list.append(sum(matrix[i]))
# sum_list = sum(sum_list)
# print(sum_list)
# print(matrix)



# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# n = int(input('Enter n: '))
# m = int(input('Enter m: '))
#
# matrix = [[randint(a, b) for i in range(n)] for j in range(m)]
# for index, values in enumerate(matrix):
#     summ_str = sum(matrix[index])
#     if matrix[index] == max(matrix):
#         print(f'Индекс максимального ряда = {index}')
# print(matrix)

#  !!!ШЕСТОЕ ЗАДАНИЕ СДЕЛАТЬ НЕ СМОГ!!!

# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# n = int(input('Enter n: '))
# m = int(input('Enter m: '))
#
# matrix = [[randint(a, b) for i in range(n)] for j in range(m)]
# for index, values in enumerate(matrix):
#     summ_str = sum(matrix[index])
#     if matrix[index] == min(matrix):
#         print(f'Индекс минимальной ряда = {index}')
# print(matrix)


#  !!!ВОСЬМОЕ ЗАДАНИЕ СДЕЛАТЬ НЕ СМОГ!!!

a = int(input('Enter a: '))
b = int(input('Enter b: '))
n = int(input('Enter n: '))
m = int(input('Enter m: '))

matrix = [[randint(a, b) for i in range(n)] for j in range(m)]
for i in range(n):
    for j in range(m):
        if j > i:
            matrix[i][j] = 0
print(matrix)
