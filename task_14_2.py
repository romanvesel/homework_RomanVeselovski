import time
import datetime

name = input('Enter your name: ')
surname = input('Enter your surname: ')
focus_time = int(input('Время фокусировки: '))
pause_time = int(input('Время перерыва: '))
counter = int(input('Количество циклов: '))

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

def Pomodoro():
    count = 0
    with open('pomodoro_log.txt', 'a+') as my_file:
        my_file.writelines(f'{name} {surname}: {datetime.datetime.now()}\n')
        my_file.close()
    while count < counter:
        print(focus(focus_time))
        print(pause(pause_time))
        count += 1
    return ' '

print(Pomodoro())
