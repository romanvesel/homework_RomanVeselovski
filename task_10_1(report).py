import csv
filename = "task_10_1.csv"
my_file = open(filename, mode='r')
group_1 = []
group_2 = []
group_3 = []
group_4 = []
group_5 = []
for rows in my_file.readlines()[1::]:
    formated = rows.strip('\n')
    formated = formated.split(',')
    if int(formated[2]) <= 12:
        group_1.append(rows.strip('\n'))
    elif 18 >= int(formated[2]) > 12:
        group_2.append(rows.strip('\n'))
    elif 25 >= int(formated[2]) > 18:
        group_3.append(rows.strip('\n'))
    elif 40 >= int(formated[2]) > 25:
        group_4.append(rows.strip('\n'))
    elif int(formated[2]) > 40:
        group_5.append(rows.strip('\n'))
print(my_file.read())

fields = ['1-12', '13-18', '19-25', '26-40', '40+']
rows = [
    group_1,
    group_2,
    group_3,
    group_4,
    group_5,
]
stat = [
    f'Количество в возрастной группе: {len(group_1)}',
    f'Количество в возрастной группе: {len(group_2)}',
    f'Количество в возрастной группе: {len(group_3)}',
    f'Количество в возрастной группе: {len(group_4)}',
    f'Количество в возрастной группе: {len(group_5)}',
        ]
new_filename = "statistics.csv"
with open(new_filename, 'w+') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerow(rows)
    csvwriter.writerow(stat)
    csvfile.close()
    