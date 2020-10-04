number_of_elements = int(input('Enter total of elements: '))
some_list = []
for i in range(number_of_elements):
    some_list.append(int(input('Enter you number: ')))
summ = 0
for el in some_list:
    if not el % 2:
        summ += 1
print(summ)



print('---------------------------')



integers = 0
some_list = []
number_of_elements = int(input('Enter total of elements: '))
while len(some_list) < number_of_elements:
    some_list.append(int(input('Enter you number: ')))
for i in some_list:
    if i % 2 == 0:
            integers += 1
print(integers)

