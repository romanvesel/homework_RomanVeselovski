import csv
fields = ['Имя', 'Фамилия', 'Возраст']
rows = [
    ['Roman', 'Veselovski', '6'],
    ['Artem', 'Ivanov', '11'],
    ['Max', 'Petrov', '21'],
    ['Irina', 'Luberec', '17'],
    ['Max', 'Ivanov', '66'],
    ['Alex', 'Varkalov', '40'],
    ['Dmitriy', 'Ivanov', '36'],
]
filename = "task_10_1.csv"
with open(filename, 'w+') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
    csvfile.close()