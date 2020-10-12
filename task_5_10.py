import datetime
from datetime import timedelta

def train_date_start(year, month, day, hour, minute):
    year = int(input('Ведите год отправления: '))
    month = int(input('Ведите месяц отправления: '))
    day = int(input('Ведите день отправления: '))
    hour = int(input('Ведите часы отправления: '))
    minute = int(input('Ведите минуты отправления: '))
    train_start = datetime.datetime(year, month, day, hour, minute)
    return train_start



def train_date_finish(year, month, day, hour, minute):
    year = int(input('Ведите год прибытия: '))
    month = int(input('Ведите месяц прибытия: '))
    day = int(input('Ведите день прибытия: '))
    hour = int(input('Ведите часы прибытия: '))
    minute = int(input('Ведите минуты прибытия: '))
    train_finish = datetime.datetime(year, month, day, hour, minute)
    return train_finish

def number_of_train():
    numb_train = input('Ведите номер поезда: ')
    return numb_train

def start_place():
    start_place = input('Ведите место отправления: ')
    return start_place


def finish_place():
    finish_place = input('Ведите место прибытия: ')
    return finish_place

def delta_time(train_start, train_finish):
    delta = train_finish - train_start
    return delta

train1_start_place = start_place()
train1_finish_place = finish_place()
train1_numb = number_of_train()
train1_start = train_date_start(0, 0, 0, 0, 0)
train1_finish = train_date_finish(0, 0, 0, 0, 0)
train_time_in_road = delta_time(train1_start, train1_finish)


train2_start_place = start_place()
train2_finish_place = finish_place()
train2_numb = number_of_train()
train2_start = train_date_start(0, 0, 0, 0, 0)
train2_finish = train_date_finish(0, 0, 0, 0, 0)
train2_time_in_road = delta_time(train2_start, train2_finish)


if train_time_in_road> timedelta(hours=7,minutes=20):
    print(f'{train1_numb} {train1_start_place}-{train1_finish_place}')



print(f'Время отправления поезда {train1_numb} {train1_start_place}-{train1_finish_place}: {train1_start}')
print(f'Время прибытия поезда {train1_numb} {train1_start_place}-{train1_finish_place}: {train1_finish}')

print(f'Время отправления поезда {train2_numb} {train2_start_place}-{train2_finish_place}: {train2_start}')
print(f'Время прибытия поезда {train2_numb} {train2_start_place}-{train2_finish_place}: {train2_finish}')
