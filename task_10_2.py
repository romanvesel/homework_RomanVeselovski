import csv

date1 = '11.06.2020'
date2 = '12.06.2020'
date3 = '13.06.2020'
date4 = '14.06.2020'
date5 = '15.06.2020'
date6 = '16.06.2020'
date7 = '17.06.2020'
rep_date = 'Средние показатели за неделю'

Mt1 = 11
Mt2 = 13
Mt3 = 14
Mt4 = 11
Mt5 = 10
Mt6 = 13
Mt7 = 12
Mt_avg = ((Mt1 + Mt2 + Mt3 + Mt4 + Mt5 + Mt6 + Mt7) / 7)

Wt1 = 9
Wt2 = 11
Wt3 = 10
Wt4 = 9
Wt5 = 12
Wt6 = 13
Wt7 = 13
Wt_avg = ((Wt1 + Wt2 + Wt3 + Wt4 + Wt5 + Wt6 + Wt7) / 7)

Mspd1 = 1
Mspd2 = 2
Mspd3 = 3
Mspd4 = 2
Mspd5 = 4
Mspd6 = 1
Mspd7 = 1
Mspd_avg = ((Mspd1 + Mspd2 + Mspd3 + Mspd4 + Mspd5 + Mspd6 + Mspd7) / 7)


Wspd1 = 2
Wspd2 = 3
Wspd3 = 1
Wspd4 = 4
Wspd5 = 1
Wspd6 = 5
Wspd7 = 2
Wspd_avg = ((Wspd1 + Wspd2 + Wspd3 + Wspd4 + Wspd5 + Wspd6 + Wspd7) / 2)

fields = ['Дата', 'Минск', 'Варшава',]
rows = [
    [date1, [f'Температура: {Mt1}°C',f'Скорость ветра: {Mspd1} км/ч'],
     [f'Температура: {Wt1}°C',f'Скорость ветра: {Wspd1} км/ч']],

    [date2, [f'Температура: {Mt2}°C', f'Скорость ветра: {Mspd2} км/ч'],
     [f'Температура: {Wt2}°C', f'Скорость ветра: {Wspd2} км/ч']],

    [date3, [f'Температура: {Mt3}°C', f'Скорость ветра: {Mspd3} км/ч'],
     [f'Температура: {Wt3}°C', f'Скорость ветра: {Wspd3} км/ч']],

    [date4, [f'Температура: {Mt4}°C', f'Скорость ветра: {Mspd4} км/ч'],
     [f'Температура: {Wt4}°C', f'Скорость ветра: {Wspd4} км/ч']],

    [date5, [f'Температура: {Mt5}°C', f'Скорость ветра: {Mspd5} км/ч'],
     [f'Температура: {Wt5}°C', f'Скорость ветра: {Wspd5} км/ч']],

    [date6, [f'Температура: {Mt6}°C', f'Скорость ветра: {Mspd6} км/ч'],
     [f'Температура: {Wt6}°C', f'Скорость ветра: {Wspd6} км/ч']],

    [date7, [f'Температура: {Mt2}°C', f'Скорость ветра: {Mspd7} км/ч'],
     [f'Температура: {Wt7}°C', f'Скорость ветра: {Wspd7} км/ч']],

    [[rep_date], [f'Температура: {Mt_avg}°C', f'Скорость ветра: {Mspd_avg} км/ч'],
    [f'Температура: {Wt_avg}°C', f'Скорость ветра: {Wspd_avg} км/ч']]
]
filename = "task_10_2.csv"
with open(filename, 'w+') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)