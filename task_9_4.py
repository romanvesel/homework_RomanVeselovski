some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def odd(func):
    def wraps(*args, **kwargs):
        new_list = []
        for i, j in enumerate(*args):
            new_list.append(j)
        return func(*new_list[::-1], **kwargs)
    return wraps

@odd
def some_func(*args, **kwargs):
    print(f'Отформатированный список - {args}')
    print(f'Остальное - {kwargs}')


some_func(some_list, a=10, c=50)
