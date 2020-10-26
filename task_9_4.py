some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def odd(func):
    def wraps(*args):
        new_list = []
        for i, j in enumerate(*args):
            new_list.append(j)
        return func(*new_list[::-1])
    return wraps

@odd
def some_func(*args):
    print(f'Отформатированный список - {args}')

some_func(some_list)