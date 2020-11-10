import time
import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('alarm_name', type=str)
parser.add_argument('alarm_time_h', type=int)
parser.add_argument('alarm_time_m', type=int)
parser.add_argument('alarm_time_s', type=int)
args = parser.parse_args()


timer_time = datetime.timedelta(hours=args.alarm_time_h, minutes=args.alarm_time_m, seconds=args.alarm_time_s)
finish_time = datetime.timedelta(hours=0, minutes=0, seconds=0)


def gen(start_time):
    while start_time > finish_time:
        time.sleep(1)
        start_time -= datetime.timedelta(seconds=1)
        yield start_time
        if start_time == finish_time:
            print('Alarm!')

g = gen(timer_time)
for i in g:
    print(i)

with open('log.txt', 'a+') as my_file:
    my_file.writelines(f'{args.alarm_name} : {datetime.datetime.now()}\n')
    my_file.close()
