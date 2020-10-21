# def check(some_word):
#     revers = some_word[::-1]
#     if some_word == revers:
#         print('Палиндром')
#     else:
#         print('Не палиндром')


# some_word = input('Enter word: ')


def check_list():
    for i, j in enumerate(some_list):
        word = some_list[i]
        if j[::-1] == word:
            print(f'{word} - Палиндром')
        else:
            print(f'{word} - Не палиндром')

some_list = ('mom', 'october', '121', '355')
check_list()
