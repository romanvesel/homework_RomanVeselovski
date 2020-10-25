# def func(**kwargs):
#     return kwargs
# print(func(a=1, b=2, c=3))


print((lambda **kwargs: {key * 2: value for key, value in kwargs.items()})(abc=5, jon=9, gh=100))