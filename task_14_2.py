import time
import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('name', type=str, help='Имя пользователя')
parser.add_argument('surname', type=str, help='Фамилия пользователя')
parser.add_argument('focus_time', type=int, nargs='?', default=25, help='Время фокусировки')
parser.add_argument('pause_time', type=int, nargs='?', default=5, help='Время паузы')
parser.add_argument('counter', type=int, nargs='?', default=4, help='Кол-во циклов')
args = parser.parse_args()


def focus(total_min):
    start_focus_time = datetime.timedelta(minutes=total_min)
    run_focus_time = datetime.timedelta(seconds=1)
    finish_focus_time = datetime.timedelta(hours=0, minutes=0, seconds=0)
    while start_focus_time > finish_focus_time:
        start_focus_time = start_focus_time - run_focus_time
        time.sleep(1)
        print(start_focus_time)
        if start_focus_time == finish_focus_time:
            print('Сделай перерыв!')
    return ' '


def pause(pause_min):
    start_pause_time = datetime.timedelta(minutes=pause_min)
    run_pause_time = datetime.timedelta(seconds=1)
    finish_pause_time = datetime.timedelta(hours=0, minutes=0, seconds=0)
    while start_pause_time > finish_pause_time:
        start_pause_time = start_pause_time - run_pause_time
        time.sleep(1)
        print(start_pause_time)
        if start_pause_time == finish_pause_time:
            print('Следующий цикл фокусировки!')
    return ' '


def pomodoro():
    count = 0
    with open('pomodoro_log.txt', 'a+') as my_file:
        my_file.writelines(f'{args.name} {args.surname}: {datetime.datetime.now()}\n')
        my_file.close()
    while count < args.counter:
        print(focus(args.focus_time))
        print(pause(args.pause_time))
        count += 1
    return ' '


print(pomodoro())
