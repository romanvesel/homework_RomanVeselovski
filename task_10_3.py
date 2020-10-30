import csv

date1 = '11.06.2020'
date2 = '12.06.2020'
date3 = '13.06.2020'
date4 = '14.06.2020'
date5 = '15.06.2020'
date6 = '16.06.2020'
date7 = '17.06.2020'

fields = ['Дата',]
rows = [
    [date1],
    [date2],
    [date3],
    [date4],
    [date5],
    [date6],
    [date7],
]
filename = "task_10_3.csv"
with open(filename, 'w+') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)