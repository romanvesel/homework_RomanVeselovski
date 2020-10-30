from datetime import datetime
filename = "task_10_3.csv"
my_file = open(filename, mode='r')
dt_list = []
for rows in  my_file.readlines()[1::]:
    rows = rows.strip('\n')
    date_format = "%d.%m.%Y"
    dt = datetime.strptime(rows, date_format)
    dt_list.append(dt)
print(min(dt_list))
print(my_file.read())