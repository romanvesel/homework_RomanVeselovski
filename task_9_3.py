some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def odd(func):
    def wraps(*args):
        new_list = []
        for i, j in enumerate(*args):
            if j % 2 == 1:
                new_list.append(j)
        return func(*new_list)
    return wraps

@odd
def some_func(*args):
    print(f'Отформатированный список - {args}')

some_func(some_list)