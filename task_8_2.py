def check(some_word):
    revers = some_word[::-1]
    if some_word == revers:
        print('Палиндром')
    else:
        print('Не палиндром')


some_word = input('Enter word: ')
check(some_word)