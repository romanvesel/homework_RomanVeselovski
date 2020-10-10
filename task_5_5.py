from random import randint

massive = []
for i in range(20):
    massive.append(randint(1, 100))
max_numb = max(massive)
print(f'Созданный массив: {massive}')

for i, j in enumerate(massive):
    if j % 2 == 0:
        massive[i] = max_numb

print(f'Новый массив:     {massive}')
print(f'Максимальное значение: {max_numb}')

