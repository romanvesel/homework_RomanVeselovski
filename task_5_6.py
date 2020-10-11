from random import randint

count = 0
massive = []
for i in range(20):
    massive.append(randint(1, 100))
print(f'Созданный массив: {massive}')

for value, j in enumerate(massive):
        if massive[value - 1] < massive[value]:
            count += 1
print(count)