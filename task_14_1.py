import time
import datetime
alarm_name = input('Enter your name: ')
alarm_time_h = int(input('Enter hours: '))
alarm_time_m = int(input('Enter min: '))
alarm_time_s = int(input('Enter sec: '))

start_time = datetime.timedelta(hours=alarm_time_h, minutes=alarm_time_m, seconds=alarm_time_s)
run_time = datetime.timedelta(seconds=1)
finish_time = datetime.timedelta(hours=0, minutes=0, seconds=0)

while start_time > finish_time:
    start_time = start_time - run_time
    time.sleep(1)
    print(start_time)
    if start_time == finish_time:
        print('Alarm!')

with open('log.txt', 'a+') as my_file:
    my_file.writelines(f'{alarm_name} : {datetime.datetime.now()}\n')
    my_file.close()